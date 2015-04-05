#!/usr/bin/env python

#Import general
import sys
import ConfigParser, os

#Import boto
import boto
from boto.s3.key import Key


def load_conf(conf_file):

    conf_path = os.path.dirname(os.path.realpath(__file__)) + conf_file

    config = ConfigParser.RawConfigParser()
    config.readfp(open(conf_path))

    parameters = {
        'AWS_ACCESS_KEY_ID': config.get("credentials", "AWS_ACCESS_KEY_ID"),
        'AWS_SECRET_ACCESS_KEY':config.get("credentials", "AWS_SECRET_ACCESS_KEY"),
    }

    return parameters

def put_in_bucket(full_file_path, name_of_file_s3, s3_bucket_name):

    parameters = load_conf("/pytos3.conf")

    conn = boto.connect_s3(parameters['AWS_ACCESS_KEY_ID'], parameters['AWS_SECRET_ACCESS_KEY'])

    s3_key = Key(conn.get_bucket(s3_bucket_name))
    s3_key.key = (name_of_file_s3)
    s3_key.set_contents_from_filename(full_file_path)

def main():

    put_in_bucket(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
