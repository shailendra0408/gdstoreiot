import json
import sys 
import os
import logging
import time
import collections
import thread


from flask import Flask
from google.cloud import datastore

#global variables declaration 
templist = []
humlist = []

#logging configuration
#@todo - need to move it to a configuration file
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('test.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


application = Flask(__name__)

@application.route("/")
def hello():
    logger.info("enter into gdstore function")
    get_gdstore_data()
    return "<h1 style='color:blue'>Hello There!</h1>"
    print "i am here"


def get_gdstore_data():
    logger.info("enter into gdstore function")
    print "enter into gdstore function"
    client = datastore.Client()
    logger.info(client)
    query = client.query(kind='senval')
    query.add_filter('Temp', '>', 2.00)
    #query.add_filter('Humidity', '>', 10.00)
    result = list(query.fetch())
    logger.info("Data fetched from server is")
    print result
    logger.info(result)
    prepare_templist(result)
    prepare_humiditylist(result)


def prepare_templist(result):
    for data in result:
        try:
            print "Temperature : {0}".format(data['Temp'])
            templist.append(data['Temp'])
            print templist 
        except KeyError:
           pass 

def prepare_humiditylist(result):
    for data in result:
        try:
            print "Humidity : {0}".format(data['Humidity '])
            humlist.append(data['Humidity '])
            print humlist
        except KeyError:
           pass




if __name__ == "__main__":
    application.run(host='0.0.0.0')
