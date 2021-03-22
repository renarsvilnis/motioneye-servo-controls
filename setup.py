import os
import subprocess
import json
import stat

def createDirectionFileIfNotExists (dirPath, direction):
  filePath = os.path.join(dirPath, f'{direction}.sh')

  # Return early if file exists
  if os.path.exists(filePath) and os.path.isfile(filePath):
    return

  commandPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'executeCommand.py')

  # Create action
  with open(filePath, "w") as f:
    f.writelines([
      "#! /usr/bin/env bash\n",
      f'python3 ${commandPath} --direction={direction}\n'
    ])
    f.close()

  # Make the new file executable by running "chmod -x" on it
  st = os.stat(filePath)
  os.chmod(filePath, st.st_mode | stat.S_IEXEC)

# Load config
with open('./config.json') as f:
  config = json.load(f)

print('Setting up motion shell scripts')
# Create executable shop for each direction
# Docs: https://github.com/ccrisan/motioneye/wiki/Action-Buttons
createDirectionFileIfNotExists(config['motionEyePath'], 'left')
createDirectionFileIfNotExists(config['motionEyePath'], 'right')
createDirectionFileIfNotExists(config['motionEyePath'], 'top')
createDirectionFileIfNotExists(config['motionEyePath'], 'bottom')


