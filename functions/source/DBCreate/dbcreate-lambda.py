import warnings
import os
import boto3
from crhelper import CfnResource
import logging
import string
import pymysql

logger = logging.getLogger(__name__)
helper = CfnResource(json_logging=True, log_level='DEBUG')


@helper.create
def create (event, context):
    try:
        db = (os.environ.get('DBName'))
        connection_config_dict = {
          'host': (os.environ.get('WPDBEndpointAddress')),
          'user': (os.environ.get('DBMasterUsername')),
          'password': (os.environ.get('DBMasterUserPassword'))
         }
        connection = pymysql.connect(**connection_config_dict)
        cursor = connection.cursor()
        cursor.execute("SET sql_notes = 0; ")
        cursor.execute('CREATE DATABASE %s' % db)
        warnings.filterwarnings("ignore", 'db')
        cursor.execute('quit')
        print(cursor.rowcount, "%s created" % db)

    except Exception as e:
        print(e)


@helper.delete
def delete(event, context):
    pass

def lambda_handler(event, context):
    helper(event, context)



