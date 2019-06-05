from google.cloud import datastore

#global variables declaration 
templist = []
humlist = []


client = datastore.Client()
query = client.query(kind='senval')
query.add_filter('Temp', '>', 2.00)
#query.add_filter('Humidity', '>', 10.00)
result = list(query.fetch())
#print result


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
    prepare_templist(result)
    prepare_humiditylist(result)
