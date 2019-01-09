"""

    The User model is managed here. It takes models.Model as its base class.

"""

from bson.objectid import ObjectId
from flask_login import UserMixin
import requests

from app import akdm, login

@login.user_loader
def load_user(_id):
    return User(_id=_id)


class User(UserMixin):

    """ We define a user model in the app that includes data from the KDM API,
    which also lets us manage user information. """

    def __init__(self, *, _id=None, username=None, password=None, token=None):
        """ Initializing a user requires a username and password. Upon init,
        the self.login() method is called, which sets self.token and the rest
        of the user object's attribs, etc.

        Also, positional arguments are banned, so be sure to use kwargs when
        initializing a user object.
        """

        self._id = _id
        self.username = username
        self.password = password
        self.token = token
        self.ui_theme = "UNDEFINED"

        # LoginManager attribs
#        self.is_authenticated = False
#        self.is_active = False
#        self.is_anonymous = False


#    def __repr__(self):
#        return self.get_id()


    def new(self):

        """ Creates a new user via API call. Always returns TWO things:
            - a boolean of whether the job was successful
            - the server's response

        """

        endpoint = akdm.config['api']['url'] + 'new/user'
        response = requests.post(
            endpoint,
            verify = akdm.config['api']['verify_ssl'],
            json= {
                'username': self.username,
                'password': self.password
            }
        )
        if response.status_code != 200:
            return False, response.text
        else:
            return True, response.text

        return False, "UNHANDLED USER CREATION ERROR"


    def login(self):
        """ Hits the /login endpoint of the API and sets the self._id and
        self.token attribute, which is currently a JWT token. """

        # set the API endpoint and POST the username/password to it
        endpoint = akdm.config['api']['url'] + 'login'
        response = requests.post(
            endpoint,
            verify = akdm.config['api']['verify_ssl'],
            json= {
                'username': self.username,
                'password': self.password
            }
        )

        # if the response is bad, return false and the response
        if response.status_code != 200:
            return False, response
        else:
            user = response.json()
            self._id = ObjectId(user['_id'])
            self.token = user['access_token']
            return True


    def get_id(self):
        """ Required for Flask-Login; also just a good idea. """
        return str(self._id)


    def refresh_token(self):
        """ Contacts the API to refresh the token. """

        # set the API endpoint and post the Authorization header to it
        endpoint = akdm.config['api']['url'] + 'authorization/refresh'
        response = requests.post(
            endpoint,
            verify = akdm.config['api']['verify_ssl'],
            headers = {'Authorization': self.token},
        )

        if response.status_code == 200:
            self.token = response.json()['access_token']
            return True

        return False


    def reset_password(self, new_password=None, recovery_code=None):
        """ Dials the API, resets the password to 'new_password' and, if
        successful, logs the user in. """

        endpoint = akdm.config['api']['url'] + 'reset_password/reset'
        response = requests.post(
            endpoint,
            verify = akdm.config['api']['verify_ssl'],
            json = {
                'username': self.username,
                'password': new_password,
                'recovery_code': recovery_code
            }
        )

        if response.status_code == 200:
            self.password = new_password
            self.login()
        else:
            return response.text

        return "UNHANDLED RESET PASSWORD ERROR"
