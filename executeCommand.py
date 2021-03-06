import json
import os
import random
import argparse
from adafruit_servokit import ServoKit

# Parse given cli arguments
# E.g python3 ./executeCommand.py --direction=up
parser = argparse.ArgumentParser()
parser.add_argument("-D", "--direction", help="Direction of travel (enum) - up,down,left,right")
# parser.add_argument("-V", "--value", help="By how many degrees (int) should move the servo in the given direction")
args = parser.parse_args()

# Load config
with open(os.path.join(os.path.dirname(__file__), 'config.json')) as f:
  config = json.load(f)

# Setup servos
servoKit = ServoKit(channels=config["channelCount"])

# Set clamping values of servos
for servoKey, servo in config["servos"].items():
  servoKit.servo[servo["port"]].set_pulse_width_range(servo["min"], servo['max'])
  # servoKit.servo[servo["port"]].angle = random.randint(servo["min"], servo['max'])

servoPositionsPath = os.path.join(os.path.dirname(__file__), 'servo-positions.json')
if os.path.exists(servoPositionsPath) and os.path.isfile(servoPositionsPath):
  with open(servoPositionsPath, 'r') as f:
    currentPosition = json.load(f)
else:
  currentPosition = {
    "pan": config["servos"]["pan"]["home"],
    "tilt": config["servos"]["tilt"]["home"]
  }

# Update positions
# TODO: not sure if need to clamp the values
if args.direction == 'left':
  currentPosition['pan'] -= config["stepSize"]
  servoKit.servo[config["servos"]["pan"]["port"]].angle = currentPosition['pan']
elif args.direction == 'right':
  currentPosition['pan'] += config["stepSize"]
  servoKit.servo[config["servos"]["pan"]["port"]].angle = currentPosition['pan']
elif args.direction == 'top':
  currentPosition['tilt'] -= config["stepSize"]
  servoKit.servo[config["servos"]["tilt"]["port"]].angle = currentPosition['tilt']
elif args.direction == 'bottom':
  currentPosition['tilt'] += config["stepSize"]
  servoKit.servo[config["servos"]["tilt"]["port"]].angle = currentPosition['tilt']

with open(servoPositionsPath, 'w') as f:
  json.dump(currentPosition, f)
