import random
import time

from paho.mqtt import client as mqtt_client
import certifi
import psutil


broker = '34106ebfef1c4ff495b80708fe6ccb73.s1.eu.hivemq.cloud'
port = 8883
topic = "led"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'afsal'
password = 'Kochi$5678'

connected = False

max_threshold = 65
min_threshold = 65


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        global connected
        connected = True
        battery = psutil.sensors_battery()
        message = "False"
        print(battery.percent)
        print(battery.power_plugged)
        print(">>>>>>>>>>>>>>>>>")
        if battery.power_plugged:
            if battery.percent >= max_threshold:
                message = "False"
            else:
                message = "True"
        else:
            if battery.percent <= min_threshold:
                message = "True"
        result = client.publish(topic, message)
    else:
        print("Failed to connect, return code %d\n", rc)


def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.tls_set(certifi.where())
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def run():
    client = connect_mqtt()
    client.loop_start()
    while not connected:
        print("connecting ....")
        time.sleep(1)


if __name__ == '__main__':
    run()
