import json

with open('credentials.json') as json_file:
    config = json.load(json_file)
    AMQPS = config.get('AMQPS')