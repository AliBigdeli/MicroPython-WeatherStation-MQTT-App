<h1 align="center">MicroPython ProMake WeatherStation MQTT App</h1>


<div align="center" ><a href="https://easy-iot.ir"><img loading="lazy" style="width:700px" src="./docs/banner.png"></a></div>

<h3 align="center">a web app application to show you the usage of webserver in micropython for reading and controlling modules</h3>
<p align="center">
<a href="https://www.micropython.org/" target="_blank"> <img src="https://micropython.org/static/img/Mlogo_138wh.png" alt="micropython" width="40" height="40"/> </a> 
<a href="https://www.easy-iot.ir/" target="_blank"> <img src="https://easy-iot.io/wp-content/uploads/2022/02/logo.png" alt="easy-iot" width="90" height="40"/> </a> 
<a href="https://gigapardaz.com/" target="_blank"> <img src="https://gigapardaz.com/wp-content/uploads/2022/05/Vector-Smart-Object.png" alt="gigapardaz" width="60" height="40"/> </a> 
<a href="https://www.raspberrypi.com/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Logo_von_Espressif.png" alt="expressif" width="70" height="40"/> </a> 
<a href="https://www.raspberrypi.com/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Mqtt-hor.svg/2560px-Mqtt-hor.svg.png" alt="mqtt" width="130" height="40"/> </a> 
</p>

### Overview
- [Features](#features)
- [Assemble](#assemble)
- [Setup](#setup)
- [Demo](#demo)
- [License](#license)
- [Bugs or Opinion](#bugs-or-opinion)


# Features
- MicroPython
- DHT
- Relay
- umqtt
- ESP32

# Assemble
as i am using the easy iot boards for development all i needed to do was to mount 2 modules on the board and get ready to use it.

<div align="center" ><img loading="lazy" style="width:700px" src="./docs/promake-esp32.jpg"></div>


# Setup
first of all you need to set the variables inside the code which includes ssid and password for connecting to a wifi as station in ```boot.py```.
```python
SSID = "wifi ssid"
PASSWORD = "wifi pass"
```
also you need to se the credentials for the mqtt broker

``` python
# MQTT Server Parameters
MQTT_CLIENT_ID = "promake-demo"
MQTT_BROKER    = "test.mosquitto.org"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "promake/receive"
```

in my usecase i have used iot mqtt panel to control the board, you can use your own application as the choice of control but based on the topics.

<div align="center" ><img loading="lazy" style="width:300px" src="./docs/index.jpg"></div>

you can see the measurements update for every 3 seconds and you can also control the relay with the button assigned to it.


# Demo
a little demonstration of the the board workflow can be found here:

<div align="center" ><img loading="lazy" style="width:720px" src="./docs/demo.gif"></div>



# License
MIT

# Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.
