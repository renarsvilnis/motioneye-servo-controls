# MotionEye Servo Controls

Add servo support to MotionEye using PCA9685 i2c board and with the help of [adafruit-circuitpython-servokit](https://github.com/adafruit/Adafruit_CircuitPython_ServoKit)

## Requirements

- Requires Python >=3.8

## Pin-hookup

Servo port mapping:

- Port 0: Tilt Sensor
- Port 1: Pan Sensor

## Setup

```bash
# Download the project
git clone git@github.com:renarsvilnis/motioneye-servo-controls.git
cd ./motioneye-servo-controls

# Install dependencies
python3 -m pip install -r requirements.txt

# Configure ./config.json file

# Do setup of shell scripts for motion
python3 ./setup.py
```
