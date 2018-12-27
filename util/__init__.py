"""
    Modules that live here are meant to be importable OUTSIDE of the app module
    as well as within it. These are the general-use support/admin methods, etc.
    of the app.

"""

from pymongo import MongoClient

MDB = MongoClient()['akdm_webapp']
