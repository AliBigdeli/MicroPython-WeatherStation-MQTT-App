from machine import Pin,reset,Timer
from umqtt import MQTTClient
from led_ctrl import PixelCtrl,Colors
from time import sleep
import ujson
import random
import dht

timer = Timer(0)

# MQTT Server Parameters
MQTT_CLIENT_ID = "promake-demo"
MQTT_BROKER    = "test.mosquitto.org"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "promake/receive"

# pin setup
pixel_obj = PixelCtrl(Pin(32,Pin.OUT),num_pixels=2)
relay_pin = Pin(26, Pin.OUT)
dht11_pin = Pin(5, Pin.IN)
dht11 = dht.DHT11(dht11_pin)
relay_pin.off()


def sub_callback(topic, msg):
  # print((topic, msg))
  str_msg = msg.decode('utf-8')
  if str_msg == "on":
    relay_pin.on()
  elif str_msg == "off":
    relay_pin.off()


def connect_and_subscribe():
  client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
  client.set_callback(sub_callback)
  client.connect()
  client.subscribe(MQTT_TOPIC)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, MQTT_TOPIC))
  pixel_obj.fill(Colors.green)
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  pixel_obj.fill(Colors.red)
  sleep(10)
  reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

def get_states(timer):
  dht11.measure()
  temp = dht11.temperature()
  humidity = dht11.humidity()
  client.publish('promake/temp',str(temp))
  client.publish('promake/humidity',str(humidity))


timer.init(period=3000, callback=get_states)


while True:
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()