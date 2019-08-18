from google.cloud import datastore
import re
#global variables declaration 
templist = []
humlist = []
datalist = []
parseddata = []

client = datastore.Client()
query = client.query(kind='Thermo')
query.add_filter('device_id', '=', '1c002e000347363339343638')
#query.add_filter('Humidity', '>', 10.00)
result = list(query.fetch(limit = 10))
#print result

def prepare_data(result):
    for data in result: 
        try:
            print "data is : {0} and published time is {1}".format(data['data'], data['published_at'])
            datalist.append(data['data'])
            parseddata = re.split(',', data['data'])
            for i in parseddata:
                print i
            #print datalist 
        except KeyError:
            pass

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
    prepare_data(result)
    #prepare_templist(result)
    #prepare_humiditylist(result)
