import network
from machine import Pin
from time import sleep
from led_ctrl import PixelCtrl,Colors

pixel_obj = PixelCtrl(Pin(32,Pin.OUT),num_pixels=2)
pixel_obj.fill(Colors.black)


SSID = "wifi ssid"
PASSWORD = "wifi pass"

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)
wlan_sta.connect(SSID, PASSWORD)

print("trying to connect to wifi")
while not wlan_sta.isconnected():
    pass

print(f"connected to {SSID}")
print(wlan_sta.ifconfig())
sleep(1)
pixel_obj.fill(Colors.blue)
sleep(1)
pixel_obj.fill(Colors.black)
