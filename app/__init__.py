"""

    This is the primary module for the flask app.

    In order for this to be imported, the following envrionment variables must
    be set:

        - API_URL
        - API_PORT (optional)
        - FLASK_ENV

    See server.sh for more information about when and how these are set.

"""

import os
import flask
from flask_login import LoginManager

# initialize the flask app; set flask 'magic' config attribs
akdm = flask.Flask(__name__)
akdm.config['SECRET_KEY'] = os.urandom(24)
akdm.config['SESSION_COOKIE_NAME'] = 'akdm_session'

# middleware
login = LoginManager(akdm)
login.login_view = 'login'
akdm.config['TESTING'] = False  # setting this to True disables @login_required

# set the API info from env variables initialized when the
#   server was started
akdm.config['api'] = {}
akdm.config['api']['verify_ssl'] = True
akdm.config['api']['url'] = "https://" + os.environ['API_URL']

if "API_PORT" in os.environ:
    akdm.config['api']['port'] = int(os.environ['API_PORT'])
    akdm.config['api']['url'] = "%s:%s/" % (
        akdm.config['api']['url'],
        akdm.config['api']['port']
    )

if os.environ['FLASK_ENV'] in ['development']:
    akdm.config['api']['verify_ssl'] = False

from app import routes
