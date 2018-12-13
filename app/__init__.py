import os
import flask

akdm = flask.Flask(__name__)
akdm.config['SECRET_KEY'] = os.urandom(24)

# set the API info from env variables initialized when the
#   server was started

akdm.config['api'] = {}
akdm.config['api']['url'] = os.environ['API_URL']
akdm.config['api']['port'] = os.environ['API_PORT']


from app import routes
