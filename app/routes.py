from app import akdm
from app.forms import LoginForm

from util import settings

import flask


#
#   Landing, downtime and login routes !
#

@akdm.route('/', methods=['GET','POST'])
def login():
#    return flask.render_template('login_downtime.html', meta=settings.get_meta_dict())
    form = LoginForm()
    if form.validate_on_submit():
        flask.flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return flask.redirect('/')
    return flask.render_template('login_open.html', meta=settings.get_meta_dict(), form=form)



#
#   Static and media routes!
#

@akdm.route('/favicon.ico')
def favicon():
    return flask.send_from_directory('static/images', 'favicon.png')

@akdm.route('/static/<sub_dir>/<path:path>')
def route_to_static(path, sub_dir):
    return flask.send_from_directory("static/%s" % sub_dir, path)


