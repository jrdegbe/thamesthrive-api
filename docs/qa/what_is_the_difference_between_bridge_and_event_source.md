# What is the difference between bridge and event source?

In the context of ThamesThrive, a bridge and an event source are two distinct components that serve different purposes in
the data processing workflow:

1. Bridge:
    - Purpose: A bridge acts as a connector or intermediary between an external data source and ThamesThrive's event
      processing system.
    - Function: Its main function is to collect data from a specific source, such as an API, queue, email, social media,
      or other external systems, and transfer that data to ThamesThrive's event sources.
    - Data Transfer: The bridge is responsible for transferring data from the external system into ThamesThrive, making it
      available for further processing within the platform.
    - Examples: ThamesThrive might come with different bridges, such as an API bridge that collects data from an API's
      endpoint or a Kafka bridge that collects data from a Kafka message broker.

2. Event Source:
    - Purpose: An event source in ThamesThrive refers to incoming traffic and represents the system or source that sends
      data to ThamesThrive for processing.
    - Function: It is responsible for receiving data from the bridge and providing ThamesThrive with a unique identifier to
      track the origin and behavior of the incoming data.
    - Data Processing: Once the data is received from the bridge, the event source handles the data, allowing ThamesThrive
      to further process and analyze it within its workflows.
    - Configuration: When setting up a new project in ThamesThrive, users must create a new event source that provides an
      identifier to be attached to track calls for data collection.
    - Authentication: Event source creates a token in form if event source id. Which is used to authorize the received data.

In summary, a bridge serves as a communication link between external data sources and ThamesThrive, enabling the transfer of
data from the external systems into the platform. On the other hand, an event source represents ThamesThrive's capability to
receive data and process it as part of its workflows, allowing for data analysis and real-time processing. The bridge is
responsible for bringing the data into ThamesThrive, while the event source handles the data once it is inside the platform.
