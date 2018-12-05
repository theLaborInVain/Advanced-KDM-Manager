#!/usr/bin/env python

from app import akdm

import configparser
import os

c_path = os.path.join(akdm.root_path, "..", "settings.cfg")
config = configparser.ConfigParser()
config.read_file(open(c_path))


def get(section,setting):
    """ Duck punches values from the config file and tries to return them in
    their native type without the user having to know their type. """

    value = config.get(section,setting,fallback=None)

    if value in ["True","False"]:
        return config.getboolean(value)

    try:
        int(value)
        return config.getint(section,setting)
    except:
        pass

    return value

def get_meta_dict():
    """ Returns a prefab/standard dictionary of application "meta" data, e.g.
    title, version, etc. used to construct basic HTML and JS elements. """

    output = {}

    # application meta data
    for key in ['title','version','api_url', 'desc', 'downtime_alert']:
        output[key] = get('application',key)

    return output
