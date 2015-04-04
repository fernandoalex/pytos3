#!/usr/bin/env python

import sys
import ConfigParser, os

def load_conf(conf_file):

    conf_path = conf_path = os.path.dirname(os.path.realpath(__file__)) + conf_file

    config = ConfigParser.RawConfigParser()
    config.readfp(open(conf_path))

    parameters = {
        'AWS_ACCESS_KEY_ID': config.get("credentials", "AWS_ACCESS_KEY_ID"),
        'AWS_SECRET_ACCESS_KEY':config.get("credentials", "AWS_SECRET_ACCESS_KEY"),
    }

    return parameters

def main():
    print load_conf("/pytos3.conf")

if __name__ == "__main__":
    main()
