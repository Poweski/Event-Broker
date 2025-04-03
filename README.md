## EN
### Description
The project is an asynchronous communication system based on a message broker, implementing an event-based publication and subscription model. The system consists of publishers (event producers) and consumers (event processors), and its architecture is consistent with the Clean Architecture principles. A reflection mechanism was used to dynamically specify channels for consumers and publishers, and event class names end with Event.

### Technologies
- Python 3
- RabbitMQ (message broker)
- Pika (library for communicating with RabbitMQ)
- Logging (monitoring events in the system)

## PL
### Opis
Projekt to asynchroniczny system komunikacji oparty na brokerze wiadomości, implementujący wydarzeniowy model publikacji i subskrypcji. System składa się z publisherów (producentów zdarzeń) i konsumentów (przetwarzających zdarzenia), a jego architektura jest zgodna z zasadami Clean Architecture. Wykorzystano mechanizm refleksji do dynamicznego określania kanałów dla konsumentów i publisherów, a nazwy klas zdarzeń kończą się na Event.

### Technologie
- Python 3
- RabbitMQ (broker wiadomości)
- Pika (biblioteka do komunikacji z RabbitMQ)
- Logging (monitorowanie zdarzeń w systemie)
