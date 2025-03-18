import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../common'))

import logging
from common.broker import MessageBroker
from consumers.domain import Type1Event

class Consumer:
    def __init__(self, broker, event_class):
        self.broker = broker
        self.event_class = event_class
        self.queue_name = event_class.__name__.lower()
        self.broker.declare_queue(self.queue_name)

    def process(self, event):
        logging.info(f'Processed {self.event_class.__name__}: {event.data}')

    def start(self):
        self.broker.consume(self.queue_name, self.process)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    broker = MessageBroker()
    event_class = Type1Event
    Consumer(broker, event_class).start()
