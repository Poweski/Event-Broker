import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../common'))

import logging
from common.broker import MessageBroker
from consumers.domain import Type3Event, Type4Event

class Consumer_Publisher:
    def __init__(self, broker, event_class1, event_class2):
        self.broker = broker
        self.event_class1 = event_class1
        self.event_class2 = event_class2
        self.queue1_name = event_class1.__name__.lower()
        self.queue2_name = event_class2.__name__.lower()
        self.broker.declare_queue(self.queue1_name)
        self.broker.declare_queue(self.queue2_name)

    def publish(self):
        event = self.event_class2({'message': f'{self.event_class2.__name__} occurred'})
        self.broker.publish(self.queue2_name, event)
        logging.info(f"Published: {event}")

    def process(self, event):
        logging.info(f'Processed {self.event_class1.__name__}: {event.data}')

    def start(self):
        self.broker.consume(self.queue1_name, self.process)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    broker = MessageBroker()
    Consumer_Publisher(broker, Type3Event, Type4Event).start()
