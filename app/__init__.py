import ssl
from flask import Flask

akdm = Flask(__name__)

from app import routes
