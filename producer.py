import pika
import json
from config_json import AMQPS

params = pika.URLParameters(AMQPS)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', 
                          routing_key='friends', 
                          body=json.dumps(body), 
                          properties=properties)
