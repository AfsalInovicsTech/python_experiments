import paho.mqtt.client as mqtt
import time

def on_connect(client, user_data, flag, rc):
    print("\nOn connect callback")
    print("\nrc: " + str(rc))
    print("\nEnd on connect")

def on_message(client, user_data, message):
    print(f"{message.payload} : is published on {message.topic}\n")


def on_publish(client, user_data, message_id):
    print(f"publishing message with id: {message_id}")

def on_subscribe(mosq, obj, mid, granted_qos):
    print(f"Subscribed: {mid} {granted_qos}")


mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect("localhost", 1883, 60)

mqttc.subscribe("maintopic/subtopic", 0)

# Publish a message
#mqttc.publish("hello/world", "my message")

# Continue the network loop, exit when an error occurs
rc = 0
counter = 0
while rc == 0:
   rc = mqttc.loop()
   mqttc.publish("maintopic/subtopic", counter)
   counter += 1
   time.sleep(1)

print("rc: " + str(rc))
