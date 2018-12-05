from app import akdm
from util import settings

from flask import render_template, send_from_directory


#
#   Landing, downtime and login routes !
#

@akdm.route('/')
def login():
#    return render_template('login_downtime.html', meta=settings.get_meta_dict())
    return render_template('login_open.html', meta=settings.get_meta_dict())



#
#   Static and media routes!
#

@akdm.route('/static/<sub_dir>/<path:path>')
def route_to_static(path, sub_dir):
    return send_from_directory("static/%s" % sub_dir, path)

