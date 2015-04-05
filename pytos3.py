#!/usr/bin/env python

#Import general
import sys
import os
import ConfigParser
import math
#from filechunkio import FileChunkIO

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

#def put_in_bucket(full_file_path, name_of_file_s3, s3_bucket_name):
def put_in_bucket(full_file_path, s3_bucket_name):
    parameters = load_conf("/pytos3.conf")

    conn = boto.connect_s3(parameters['AWS_ACCESS_KEY_ID'], parameters['AWS_SECRET_ACCESS_KEY'])
    conn_bucket = conn.get_bucket(s3_bucket_name)

    # What's the file size
    file_size = os.stat(full_file_path).st_size

    multi_part_upload = conn_bucket.initiate_multipart_upload(os.path.basename(full_file_path))

    #chunk size in MB needs to be => than 10MB
    chunk_size_MB = 10
    # chunk size to be used
    chunk_size = chunk_size_MB * 1024 * 1024

    # Divide in how many pieces
    chunk_count = int(math.ceil(file_size / float(chunk_size)))

    for i in range(chunk_count):
        #set the byte to start upload
        offset = chunk_size * i

        #how many bytes to upload this time chunk_size or less than that
        bytes = min(chunk_size, file_size - offset)

        #with FileChunkIO(full_file_path, 'r', offset = offset, bytes = bytes) as fp:
        #https://github.com/piotrbulinski/boto/commit/c3b81eb115e469b9df1ff8c379d3208327da2c84
        with open(full_file_path, 'rb') as fp:
            fp.seek(offset)
            multi_part_upload.upload_part_from_file(fp, part_num = i + 1, size = bytes)

    multi_part_upload.complete_upload()

def main():

    put_in_bucket(sys.argv[1], sys.argv[2])
    #put_in_bucket(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
