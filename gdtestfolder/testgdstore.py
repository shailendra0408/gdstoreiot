from google.cloud import datastore

datastore_client = datastore.Client()

kind = 'senval'
name = 'test4'
task_key = datastore_client.key(kind, name)

task = datastore.Entity(key = task_key) 
task['Temp'] = 11.09 

datastore_client.put(task)

print('Saved {}:{}'.format(task.key, task['Temp']))

key = datastore_client.key('senval', 'test1')
task = datastore_client.get(key)
print "printing taks "
print task 

query = datastore_client.query( kind = 'senval') 
query.add_filter ('Temp', '>', 20)
results = list(query.fetch())
print results

for key in results:
    print value 


