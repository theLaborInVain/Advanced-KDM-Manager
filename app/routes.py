"""

    All webbapp reoutes are managed here. DO NOT create routes outside of this
    module.

"""


import flask
import requests

from app import akdm
from app.forms import LoginForm

from util import settings

#
#   Login application!
#

@akdm.route('/', methods=['GET', 'POST'])
@akdm.route('/login', methods=['GET', 'POST'])
def login():

    """ This is the main route/endpoint for logging into the app. """

    # uncomment to force a downtime (i.e. disable the login controls)
#    return flask.render_template(
#        'login_downtime.html',
#        api=None,
#        meta=settings.get_meta_dict()
#    )

    # check if the API is alive and listening; if not, show the downtime screen
    try:
        request = requests.get(
            akdm.config['api']['url'] + "stat",
            verify=akdm.config['api']['verify_ssl']
        )
        akdm.config['api']['version'] = request.json()['meta']['api']['version']
    except requests.exceptions.ConnectionError as requests_exception:
        akdm.logger.error(requests_exception)
        return flask.render_template(
            'login_downtime.html',
            api=None,
            meta=settings.get_meta_dict()
        )

    # if we're not doing a downtime and the API is alive, render the login
    # panel and controls
    form = LoginForm()
    if form.validate_on_submit():
        akdm.logger.info("HERE")
        flask.flash(
            'Login requested for user {}, remember_me={}'.format(
                form.username.data,
                form.remember_me.data
            )
        )
        return flask.redirect('/dashboard')

    return flask.render_template(
        'login_open.html',
        api=akdm.config['api'],
        meta=settings.get_meta_dict(),
        form=form
    )


#
#   Actual application!
#

@akdm.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    """ This is the real app. We use flask to manage the "session", but
    everything else is between the user and the API (via angular code in the
    HTML doc we return. """

    return flask.render_template(
        'login_downtime.html',
        api=akdm.config['api'],
        meta=settings.get_meta_dict()
    )



#
#   Static and media routes for dev use!
#

@akdm.route('/favicon.ico')
def favicon():
    """ Returns the favicon when working in dev. """
    return flask.send_from_directory('static/images', 'favicon.png')

@akdm.route('/static/<sub_dir>/<path:path>')
def route_to_static(path, sub_dir):
    """ Returns the static dir when working in dev. """
    return flask.send_from_directory("static/%s" % sub_dir, path)
