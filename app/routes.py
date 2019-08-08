"""

    All webbapp reoutes are managed here. DO NOT create routes outside of this
    module.

"""


import flask
import flask_login
import requests
import werkzeug

from app import akdm
from app.forms import LoginForm, SignupForm, ResetForm

from app.models import users

import util
from util import settings


#
#   Login application!
#

@akdm.route('/', methods=['GET', 'POST'])
@akdm.route('/index', methods=['GET', 'POST'])
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
    util.stat_api()

    # before playing with forms or anything, see if we've got an active user
    if flask_login.current_user.is_authenticated:
        akdm.logger.info(
            "redirecting authenticated user: %s" % flask_login.current_user
        )
        return flask.redirect(flask.url_for('dashboard'))

    # check for LoginForm input; if we've got it, try to log a user in and, if
    # they're trying to get somewhere else, send them there
    form = LoginForm()
    if form.validate_on_submit():
        user = users.User(username=form.username.data, password=form.password.data)
        user.login()
        if user._id is not None and user.token is not None:

            # authenticate the user and log them in
            flask_login.login_user(user, remember=form.remember_me.data)

            # handle 'next' page if we're stopping them to login first
            next_page = flask.request.args.get('next')
            if not next_page or werkzeug.urls.url_parse(next_page).netloc != '':
                next_page = flask.url_for('dashboard')

            # create the response and set the JWT token in the cookie
            redirect = flask.redirect(next_page)
            response = akdm.make_response(redirect)
            response.set_cookie('akdm_token', user.token)
            return response
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
    flask_login.logout_user()
    redirect = flask.redirect(flask.url_for('login'))
    response = akdm.make_response(redirect)
    response.set_cookie('akdm_token', 'None')
    return response


@akdm.route('/register', methods=['GET','POST'])
def register():
    """ Shows and processes the signup form """

    util.stat_api()

    form = SignupForm()

    if flask.request.method == 'POST' and form.validate():
        user = users.User(username=form.username.data, password=form.password.data)
        success, api_response = user.new()
        if success:
            flask.flash('Registration successful! Please sign in!')
            return flask.redirect(flask.url_for('login'))
        else:
            flask.flash(api_response)

    return flask.render_template(
        'register.html',
        api=akdm.config['api'],
        meta=settings.get_meta_dict(),
        form=form
    )


@akdm.route('/reset_password', methods=['GET','POST'])
def reset_pw():
    """ Shows and processes the password reset form. """

    util.stat_api()

    form = ResetForm()

    if flask.request.method == 'POST' and form.validate():
        user = users.User(username=form.username.data)
        reset_result = user.reset_password(
            new_password = form.password.data,
            recovery_code = flask.request.args.get('recovery_code')
        )

        # user.reset_password() logs the user in, so we should have an _id and
        # a self.token now, which we can use to log us into AKDMM
        if user._id is not None and user.token is not None:
            flask_login.login_user(user, remember=form.remember_me.data)
            next_page = flask.url_for('dashboard')
            redirect = flask.redirect(next_page)
            response = akdm.make_response(redirect)
            response.set_cookie('akdm_token', user.token)
            return response
        else:
            flask.flash(reset_result)

    return flask.render_template(
        'reset_password.html',
        api=akdm.config['api'],
        meta=settings.get_meta_dict(),
        form=form
    )



#
#   Actual application!
#

@akdm.route('/dashboard', methods=['GET', 'POST'])
@flask_login.login_required
def dashboard():

    """ This is the real app. We use flask to manage the "session", but
    everything else is between the user and the API (via angular code in the
    HTML doc we return. """

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
