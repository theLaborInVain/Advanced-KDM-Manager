"""

    All webbapp reoutes are managed here. DO NOT create routes outside of this
    module.

"""


import flask
import flask_login
import requests
import werkzeug

from app import akdm
from app.forms import LoginForm

from app.models import users

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

    # before playing with forms or anything, see if we've got an active user
    if flask_login.current_user.is_authenticated:
        akdm.logger.info("current user is authenticated redirecting: %" % flask_login.current_user)
        return flask.redirect(flask.url_for('dashboard'))

    # check for LoginForm input; if we've got it, try to log a user in and, if
    # they're trying to get somewhere else, send them there
    form = LoginForm()
    if form.validate_on_submit():
        user = users.User(username=form.username.data, password=form.password.data)
        user.login()
        if user._id is not None and user.token is not None:
            flask_login.login_user(user, remember=form.remember_me.data)
            akdm.logger.info("successful auth: %s|%s" % (user, flask_login.current_user))
            next_page = flask.request.args.get('next')
            if not next_page or werkzeug.urls.url_parse(next_page).netloc != '':
                next_page = flask.url_for('dashboard')
            return flask.redirect(next_page)
        else:
            flask.flash('Invalid username or password!')
            return flask.redirect(flask.url_for('login'))

    # finally, if we failed to log a user in and the API is alive, show the main
    # login app/form
    return flask.render_template(
        'login_open.html',
        api=akdm.config['api'],
        meta=settings.get_meta_dict(),
        form=form
    )


@flask_login.login_required
@akdm.route('/logout')
def logout():
    """ Kills the flask_login 'session' and returns the user to the login. """
    akdm.logger.warn(flask_login.current_user.get_id())
    flask_login.logout_user()
    return flask.redirect(flask.url_for('/'))


#
#   Actual application!
#

@akdm.route('/dashboard', methods=['GET', 'POST'])
@flask_login.login_required
def dashboard():

    """ This is the real app. We use flask to manage the "session", but
    everything else is between the user and the API (via angular code in the
    HTML doc we return. """

    akdm.logger.info("current_user: %s" % dir(flask_login.current_user))
    return flask.render_template(
        'dashboard.html',
        api=akdm.config['api'],
        meta=settings.get_meta_dict(),
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
