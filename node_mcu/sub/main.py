import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
from machine import Pin
import onewire
import ds18x20
esp.osdebug(None)
import gc
gc.collect()
from machine import Pin
led = Pin(2, Pin.OUT)


last_message = 0
message_interval = 5
counter = 0

ssid = 'KERALA VISION'
password = '22334455'
mqtt_server = '34106ebfef1c4ff495b80708fe6ccb73.s1.eu.hivemq.cloud'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.106'

client_id = ubinascii.hexlify(machine.unique_id())

topic_pub_temp = b'esp/ds18b20/temperature'

last_message = 0
message_interval = 5

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

def sub_cb(topic, msg):
  print((topic, msg))
  
  if topic == b'led':
      if msg == b'True':
          led.off()
      else:
          led.on()


def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server, user="afsal", password="Kochi$5678", ssl=True, ssl_params={"server_hostname": "34106ebfef1c4ff495b80708fe6ccb73.s1.eu.hivemq.cloud"})
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe("led")
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, "led"))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      msg = b'Hello #%d' % counter
      client.publish("my/test/topic", msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()
