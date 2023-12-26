# What is event source?

Event source refers to incoming traffic, which consists of systems that are capable of
sending data to ThamesThrive. These systems can include websites, internal systems, and various services. ThamesThrive
identifies and logs this inbound traffic, assigning it a unique identifier to track its origin and behavior.

An event source serves as a bridge between the external system and ThamesThrive. It collects data from a specific source,
such as a queue, email, or social media, and transfers it to ThamesThrive for further processing. For instance, ThamesThrive can
use an API bridge to collect data from an API's "/track" endpoint and bring it into the system. Depending on the version
of ThamesThrive being used, there may be different types of bridges, such as a Kafka bridge, designed to collect data from a
Kafka message broker.

When setting up a new project with ThamesThrive, it is essential to create a new event source. This event source provides an
identifier that can be attached to track calls, enabling the collection of data about users. However, it's worth noting
that an event source can be configured as ephemeral, meaning the data received through this type of event source is not
stored permanently in the system. Instead, it is used and processed by the workflow in real-time, without the need for
long-term storage.

Important to consider is that certain sources may require user consent before collecting and storing their data. For
example, a web page might need user consent to gather and retain their data for processing.
