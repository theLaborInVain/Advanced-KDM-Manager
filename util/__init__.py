"""
    Modules that live here are meant to be importable OUTSIDE of the app module
    as well as within it. These are the general-use support/admin methods, etc.
    of the app.

"""

from pymongo import MongoClient
import requests

from app import akdm

MDB = MongoClient()['akdm_webapp']

def stat_api():

    """ Hits the api's 'stat' endpoint or dies trying. Updates the app config OR
    returns an exception. """

    try:
        request = requests.get(
            akdm.config['api']['url'] + "stat",
            verify = akdm.config['api']['verify_ssl'],
            headers = {"API-Key": "AKDMM"},
        )
        akdm.config['api']['version'] = request.json()['meta']['api']['version']
        return True
    except requests.exceptions.ConnectionError as requests_exception:
        akdm.logger.error(requests_exception)
        return flask.render_template(
            'login_downtime.html',
            api=None,
            meta=settings.get_meta_dict()
        )

    raise
