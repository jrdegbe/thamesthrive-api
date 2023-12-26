This documentation describes the Memory Payload Collector action node, which is used to collect input payloads in a defined key inside a memory object. The memory object is kept inside the workflow and can be referenced with the Copy Data plugin or any dotted notation string, such as memory@defined_key.

The Memory Payload Collector node can be connected to multiple nodes, meaning that it will be executed as many times as there are nodes connected to it at the input port. Each of the preceding nodes sends the result of its operation (payload) to the Memory Payload Collector node, which collects the payloads and saves them in the memory object under the given key.

The Memory Payload Collector node supports two types of connections: list type and dictionary type. The list type allows all incoming payloads to be seen in a list, while the dictionary type combines all incoming payloads into a dictionary type, where the key for each payload is the name of the connection (called sometimes graph edge) it came from.

The Memory Payload Collector node also supports advanced configuration, which allows users to specify the name (key in memory object) that will hold the collected payloads, as well as the type of collection (list or dict). This advanced configuration is specified in a JSON format.

