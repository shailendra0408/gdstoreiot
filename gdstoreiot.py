import json
import sys 
import os
import logging
import time
import collections
import thread
import re 


from flask import Flask, render_template, request, redirect, url_for, escape, session, make_response, request, jsonify  
from google.cloud import datastore



#global variables declaration 
templist = []
humlist = []
dewlist = []
PM1list = []
PM25list = []
PM10list = []
datalist = []
parseddata = []

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

application.secret_key = "saksh2iuyw2klhqwshswi"

@application.route("/", methods = ['GET', 'POST'])
def landingPage():
    logger.info("inside / handler")
    return render_template("index.html", user = "")

@application.route("/testapi1", methods = ['GET', 'POST'])
def testapi1():
    if request.method == "POST" :
        message = "Huston,i got a hit from frontend - what to do next bla bla bla"
        logger.info("inside testapi1 function")
        content = request.get_json(force=True)
        print content
        print message 
        hello()
        print templist
        print humlist
        return json.dumps({"result":"Success", "response_content":templist })




#@application.route("/userverifictaion", methods = ['GET', 'POST'])
#def userverification():
#    if request.method == "POST" :
#        logger.info("Inside userverification method")
#        user_emailid = 0
#        user_pass    = 0
#        user_emailid = request.form['user_emailid']
#        user_pass    = request.form['user_pass']
#        logger.debug('email id is %s and %s', user_emailid, user_pass)
#        user_exist = check_if_user_exist (user_emailid, user_pass)

#def check_if_user_exist(emailid,upassword)
#    logger.info("Inside check_if_user_exist function")
#    query_user_exist = """SELECT * FROM ADMIN_DATA WHERE EMAIL_ID = %s"""
#    args = (emailid)
    

@application.route("/gdstoretest")
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
    query = client.query(kind='Thermo')
    query.add_filter('device_id', '=', '1c002e000347363339343638')
    result = list(query.fetch(limit = 1000))
    logger.info("Data fetched from server is")
    prepare_data(result)
    
def prepare_data(result):
    for data in result: 
        try:
            print "data is : {0} and published time is {1}".format(data['data'], data['published_at'])
            time = data['published_at']
            datalist.append(data['data'])
            parseddata = re.split(',', data['data'])
            prepare_humiditylist(parseddata, time) 
            prepare_templist(parseddata, time)
            prepare_dewlist(parseddata, time)
            prepare_pm1list(parseddata, time)
            prepare_pm25list(parseddata, time)
            prepare_pm10list(parseddata, time)
            
        except KeyError:
            pass


def prepare_humiditylist(parseddata,time ):
    Humidity = parseddata[0]
    Humidity = re.split('=', Humidity)
    Humidity = Humidity[1]
    humiditydict = {}
    humiditydict.update({"time":time})
    humiditydict.update({"humidity": Humidity})
    humlist.append(humiditydict)
    print "Humidity List is {0} \r\n ".format( humlist )

def prepare_templist(parseddata,time):
    Temperature = parseddata[1]
    Temperature = re.split('=', Temperature)
    Temperature = Temperature[1]
    tempdict = {}
    tempdict.update({"time": time})
    tempdict.update({"temperature": Temperature})
    templist.append(tempdict)
    print "Temperature list is {0}".format( templist )

def prepare_dewlist(parseddata,time):
    Dew = parseddata[2]
    Dew = re.split('=', Dew)
    Dew = Dew[1]
    dewdict = {}
    dewdict.update({"time" :time})
    dewdict.update({"dew" : Dew})
    dewlist.append(dewdict)
    print "Dew List is {0}".format( dewlist )

def prepare_pm1list(parseddata, time):
    PM1 = parseddata[3]
    PM1 = re.split('=', PM1)
    PM1 = PM1[1]
    pm1dict = {}
    pm1dict.update({"time" : time})
    pm1dict.update({"pm1" : PM1})
    PM1list.append(pm1dict)
    print "PM1 list is {0}".format(PM1list)

def prepare_pm25list(parseddata, time):
    PM25 = parseddata[4]
    PM25 = re.split('=', PM25)
    PM25 = PM25[1]
    pm25dict = {}
    pm25dict.update({"time" : time})
    pm25dict.update({"pm25" : PM25})
    PM25list.append(pm25dict)
    print "PM25 list is {0}".format(PM25list)

def prepare_pm10list(parseddata, time):
    PM10 = parseddata[5]
    PM10 = re.split('=', PM10)
    PM10 = PM10[1]
    pm10dict = {}
    pm10dict.update({"time" : time})
    pm10dict.update({"pm10" : PM10})
    PM10list.append(pm10dict)
    print "PM10 list is {0}".format(PM10list)            



if __name__ == "__main__":
    application.run(host='0.0.0.0')
