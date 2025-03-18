import pika
import json
import logging

class Event:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"{self.__class__.__name__}(data={self.data})"

class MessageBroker:
    def __init__(self, host='localhost'):
        self.host = host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def publish(self, queue_name, event):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(event.__dict__))
        logging.info(f'Published {event.__class__.__name__} to {queue_name}')

    def consume(self, queue_name, callback):
        def wrapper(ch, method, properties, body):
            data = json.loads(body)
            event_class = globals().get(queue_name + 'Event')
            event = event_class(data) if event_class else Event(data)
            callback(event)

        self.channel.basic_consume(queue=queue_name, on_message_callback=wrapper, auto_ack=True)
        logging.info(f'Started consuming {queue_name}')
        self.channel.start_consuming()
