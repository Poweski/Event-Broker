import time
import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../common'))

import logging
from common.broker import MessageBroker
from publishers.domain.type_3_event import Type3Event

class Publisher:
    def __init__(self, broker, event_class):
        self.broker = broker
        self.event_class = event_class
        self.queue_name = event_class.__name__
        self.broker.declare_queue(self.queue_name)

    def start(self):
        while True:
            event = self.event_class({'message': f'{self.event_class.__name__} occurred'})
            self.broker.publish(self.queue_name, event)
            delay = random.randint(1, 10)
            logging.info(f'Published {self.queue_name}, sleeping for {delay} seconds')
            time.sleep(delay)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    broker = MessageBroker()
    Publisher(broker, Type3Event).start()
