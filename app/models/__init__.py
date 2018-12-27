"""

    The base class for all models used by the webapp lives here.

"""

import util

class Model:

    """ We define a user model in the app that includes data from the KDM API,
    which also lets us manage user information. """

    def __init__(self, _id=None, collection=None):

        """ Checks for mandatory attributes. Runs self.load() to set attributes
        and the self.collection dictionary. """

        for attrib in ['_id', 'collection']:
            if not hasattr(self, attrib):
                raise AttributeError('Models must be initialized with the %s\
                attribute!')

        if _id is not None:
            self._id = _id

        if collection is not None:
            self.collection = collection

        self.load()


    def load(self):

        """ This is the generic load method for all models. It uses self._id and
        self.collection to find the doc in the MDB for the requested object and
        sets self.doc to be that dict. """

        self.doc = util.mdb[self.collection].find_one({'_id': self._id})


    def save(self):

        """ Saves self.doc back to the mdb for self.collection. """

        util.MDB[self.collection].save(self.doc)
