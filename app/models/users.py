"""

    The User model is managed here. It takes models.Model as its base class.

"""

from . import Model

class User(Model):

    """ We define a user model in the app that includes data from the KDM API,
    which also lets us manage user information. """

    def __init__(self, *args, **kwargs):

        """ Generic __init__() method that sets the mandatory attribs and
        uses the base class load() method to initialize itself. """

        self.collection = 'users'
        super(User, self).__init__(*args, **kwargs)

    def new(self):

        """ Creates a new user, saves it to the MDB, calls the base class
        load() method, i.e. initializes the object. """

        self.save()
