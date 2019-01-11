"""

    Convenience methods for getting at application settings live here.

    Important! Whenever this module is imported, it has an attribute
    called CONFIG, which is created by running initialize_config().

    The initialize_config() method is what determines which settings file
    gets read, i.e. "settings.cfg" or "private.cfg", so you may need
    to run that AGAIN after importing to make sure that you're getting the
    config settings you want.

"""

import configparser
import os

from app import akdm


def initialize_config(private=False):
    """ Parses the 'settings.cfg' file and returns a configparser object. """
    if private:
        c_path = os.path.join(akdm.root_path, "..", "private.cfg")
    else:
        c_path = os.path.join(akdm.root_path, "..", "settings.cfg")
    config = configparser.ConfigParser()
    config.read_file(open(c_path))
    return config

CONFIG = initialize_config()


#
#   General usage methods for settings and settings-related info.
#

def get(section, setting):
    """ Duck punches values from the config file and tries to return them in
    their native type without the user having to know their type. """

    value = CONFIG.get(section, setting, fallback=None)

    if value in ["True", "False"]:
        return CONFIG.getboolean(section, setting)

    try:
        int(value)
        return CONFIG.getint(section, setting)
    except ValueError:
        pass

    return value


def get_meta_dict():
    """ Returns a prefab/standard dictionary of application "meta" data, e.g.
    title, version, etc. used to construct basic HTML and JS elements. """

    output = {}
    for key in CONFIG.items('application'): # these are tuples
        output[key[0]] = get('application', key[0])
    return output
