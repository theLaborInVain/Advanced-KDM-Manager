import os
import flask

akdm = flask.Flask(__name__)
akdm.config['SECRET_KEY'] = os.urandom(24)

# set the API info from env variables initialized when the
#   server was started

akdm.config['api'] = {}
akdm.config['api']['verify_ssl'] = True
akdm.config['api']['url'] = "https://" + os.environ['API_URL'] 

if "API_PORT" in os.environ:
    try:
        port = int(os.environ['API_PORT'])
        akdm.config['api']['port'] = port
        akdm.config['api']['url'] = "%s:%s/" % (akdm.config['api']['url'], port)
    except:
        akdm.config['api']['url'] += '/'

if os.environ['FLASK_ENV'] in ['development']:
    akdm.config['api']['verify_ssl'] = False

from app import routes
