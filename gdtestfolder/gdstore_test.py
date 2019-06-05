from google.cloud import datastore
client = datastore.Client()
query = client.query(kind='senval')
query.add_filter('Temp', '>', 2.00)
#query.add_filter('Humidity', '>', 10.00)
result = list(query.fetch())
print result

for data in result:
    try:
        print "Temperature : {0}".format(data['Temp'])
        print "Humidity : {0}".format(data['Humidity '])
    except KeyError:
       pass 
