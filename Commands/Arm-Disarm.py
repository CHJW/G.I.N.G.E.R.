import argparse
import json
import requests

# Instantiate the parser
parser = argparse.ArgumentParser(description='G.I.N.G.E.R. Arm-Disarm Command')

parser.add_argument('-arm', dest='arm', action='store_true', help='arm the component')
parser.add_argument('-disarm', dest='arm', action='store_false', help='disarm the component')
parser.add_argument('-config', type=str, required=True,
                    help='input textfile with configuration for arming/disarming')
parser.set_defaults(arm=True)

# Parse the Arguments
args = parser.parse_args()

# Read in config file
fd = open(args.config, 'r')
json_data = json.load(fd)

# Perform request
response = None
if (args.arm):
    print('sending request for arm to hook server')
    response = requests.post(json_data['arm']['url'], json=json_data['arm']['data'])
else:
    print('sending request for disarm to hook server')
    response = requests.post(json_data['disarm']['url'], json=json_data['disarm']['data'])

print('response from hook server: ' + response.text)
