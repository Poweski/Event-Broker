import time
import logging
from publishers.domain.type_1_event import Type1Event
from common.broker import MessageBroker

class Publisher:
    def __init__(self, broker, event_class):
        self.broker = broker
        self.event_class = event_class
        self.queue_name = event_class.__name__.lower()
        self.broker.declare_queue(self.queue_name)

    def start(self):
        while True:
            event = self.event_class({'message': f'{self.event_class.__name__} occurred'})
            self.broker.publish(self.queue_name, event)
            logging.info(f"Published: {event}")
            time.sleep(2)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    broker = MessageBroker()
    Publisher(broker, Type1Event).start()
