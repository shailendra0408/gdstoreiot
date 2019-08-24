from google.cloud import datastore
import re

#global variables declaration of list  
templist = []
humlist = []
dewlist = []
PM1list = []
PM25list = []
PM10list = []
datalist = []
parseddata = []

client = datastore.Client()
query = client.query(kind='Thermo')
query.add_filter('device_id', '=', '1c002e000347363339343638')
#query.add_filter('Humidity', '>', 10.00)
result = list(query.fetch(limit = 10))
#print result


#add one function to massage the data and return a dictionary with Variable, Time stamp 
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
    prepare_data(result)
    #prepare_templist(result)
    #prepare_humiditylist(result)
