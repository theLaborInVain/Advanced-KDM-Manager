import os
from flask import Flask

akdm = Flask(__name__)
akdm.config['SECRET_KEY'] = os.urandom(24)

from app import routes
