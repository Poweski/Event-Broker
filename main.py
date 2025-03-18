import subprocess
import os

from publishers.app.type_1_event_publisher import Publisher
from publishers.app.type_2_event_publisher import Publisher
from publishers.app.type_3_event_publisher import Publisher

from consumers.app.type_1_event_consumer import Consumer
from consumers.app.type_2_event_consumer import Consumer
from consumers.app.type_3_event_consumer import Consumer_Publisher
from consumers.app.type_4_event_consumer import Consumer

def run_scripts():
    processes = []
    
    scripts = {
        'publishers': [
            os.path.join(os.getcwd(), "publishers", "app", "type_1_event_publisher.py"),
            os.path.join(os.getcwd(), "publishers", "app", "type_1_event_publisher.py"),
            os.path.join(os.getcwd(), "publishers", "app", "type_1_event_publisher.py"),
            os.path.join(os.getcwd(), "publishers", "app", "type_2_event_publisher.py"),
            os.path.join(os.getcwd(), "publishers", "app", "type_3_event_publisher.py")
        ],
        'consumers': [
            os.path.join(os.getcwd(), "consumers", "app", "type_1_event_consumer.py"),
            os.path.join(os.getcwd(), "consumers", "app", "type_1_event_consumer.py"),
            os.path.join(os.getcwd(), "consumers", "app", "type_2_event_consumer.py"),
            os.path.join(os.getcwd(), "consumers", "app", "type_3_event_consumer.py"),
            os.path.join(os.getcwd(), "consumers", "app", "type_4_event_consumer.py")
        ]
    }
    
    for i in range(1):
        script = scripts['publishers'][i % len(scripts['publishers'])]
        print(f"Starting publisher {i+1}: {script}")
        process = subprocess.Popen(["python", script])
        processes.append(process)
    
    for i in range(1):
        script = scripts['consumers'][i % len(scripts['consumers'])]
        print(f"Starting consumer {i+1}: {script}")
        process = subprocess.Popen(["python", script])
        processes.append(process)
    
    for process in processes:
        process.wait()

if __name__ == "__main__":
    run_scripts()
