import json
import math
import time
import paho.mqtt.client as mqtt 
import socket

timestamp = math.trunc(time.time())
localhost = socket.gethostbyname(socket.gethostname())
print (localhost)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_publish(client, userdata, mid):
    print("Message published")

data = {
	"category":"REAL",
	"datatype":"FLOAT",
	"name":"SensorTag2",
	"timestamp":timestamp,
	"value":92.5,
	"quality":"GOOD (0)",
	"address":"DCS/path/to/tag"
}


datasend = json.dumps(data)
print (datasend)

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# connect to localhost
print("Connecting to server")
client.connect(localhost)

# starting loop
client.loop_start()
print ("Starting for loop")
value = 92.5

for i in range(1,5):
	print "publish value: ", value
	client.publish("TestTopic1", value)
	value += 1

client.loop_stop()

