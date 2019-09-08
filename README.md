# gdstoreiot
Repo for 
* Using google data store for storing data pushed by a IoT device ( virtual or real device) 
* Developing a small UI to display real time data

## Status Quo 
Currently this is very limited edition of what can be done. There are lot of to-do's in queue for example 
* using the google IoT core 
* using google pub-sub to push data to google IoT core 
* using google big query with the data ( push data to google big query and then run google big queries to fetch intersting data)
* use T[ensor flow](https://www.tensorflow.org/) on top of this data 
* use RPI along with a sensor to push real data
* probably use [Yuktix](https://www.yuktix.com/) API to push and store real time sensor data. 
* develop a small UI for selecting the devices 
* If not Yuktix, then expose the REST API to develop other app's. 

## GreenSense Dashboard 
At Yuktix we are already developing a dashboard that would be highly interactive and would have lot of features, but just as a excersie, i wanted to develop a dashboard specifically for Agriculture. 

## Remote Control Dashbaord 
RPI Control repo that i have published long back has very limited features, probably using the google data store or google IoT core, improve the repo and deploy the system somewhere in the house. Of-course, i have never talked about the security aspects on IoT which is a major concern when someone is doing remote control, i have to add that too. The best way would be to use OTP based login everytime ( probably add both email and SMS based OTP). 



