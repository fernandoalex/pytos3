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

def put_in_bucket(file):

    file_path = os.path.dirname(os.path.realpath(__file__)) + file

    parameters = load_conf("/pytos3.conf")

    conn = boto.connect_s3(parameters['AWS_ACCESS_KEY_ID'], parameters['AWS_SECRET_ACCESS_KEY'])

    #Create a key to word with s3
    s3_key = Key(conn.get_bucket('pytos3-backup'))
    s3_key.key = ('teste.txt')
    s3_key.set_contents_from_filename(file_path)

def main():
    put_in_bucket("/teste1.txt")

if __name__ == "__main__":
    main()
