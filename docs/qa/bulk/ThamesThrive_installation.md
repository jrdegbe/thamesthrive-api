# How can ThamesThrive be installed as a Docker container?

- ThamesThrive can be easily installed as a Docker container by following the provided instructions.

# What are the dependencies for running ThamesThrive?

- ThamesThrive requires Elasticsearch, Redis, ThamesThrive API, and ThamesThrive GUI to run. Docker containers need to be started
  for each of these services.

# How can I start the Elasticsearch database for ThamesThrive?

- The Elasticsearch database for ThamesThrive can be started by pulling and running the Elasticsearch single-node Docker
  image with the provided command.

# How can I start the Redis instance for ThamesThrive?

- The Redis instance for ThamesThrive can be started by running the Redis Docker container with the provided command.

# How can I start the ThamesThrive API?

- The ThamesThrive API can be started by pulling and running the ThamesThrive API Docker image with the provided command. Make
  sure to set the necessary environment variables, such as the Elastic host and Redis host.

# How can I connect ThamesThrive to Elasticsearch via SSL?

- If you have an Elasticsearch instance and want to connect to it via HTTPS, you can use the provided command with the
  necessary environment variables set accordingly.

# How can I start the ThamesThrive GUI?

- The ThamesThrive GUI can be started by pulling and running the ThamesThrive GUI Docker image with the provided command.

# How can I run the import worker in ThamesThrive?

- To run the import worker in ThamesThrive, you can use the provided command to start the worker Docker container. Make sure
  to set the Redis host accordingly.

# How can I access the ThamesThrive Graphical User Interface (GUI)?

- The ThamesThrive GUI can be accessed by visiting the provided URL and following the instructions for ThamesThrive setup. Make
  sure to specify the ThamesThrive API URL correctly.

# Where can I find the system documentation for ThamesThrive?

- The system documentation for ThamesThrive can be accessed by visiting the provided URL. Make sure the documentation Docker
  is started.

# Where can I find the API documentation for ThamesThrive?

- The API documentation for ThamesThrive can be accessed by visiting the provided URL.

# How can I specify a specific version when installing ThamesThrive?

- To install a specific version of ThamesThrive, you can add a version tag to the Docker image name in the command, such
  as `ThamesThrive/ThamesThrive-api:<version>` or `ThamesThrive/ThamesThrive-gui:<version>`.

# What is the purpose of running multiple instances of Elasticsearch in ThamesThrive?

- Running multiple instances of Elasticsearch in ThamesThrive is not a production solution but can be done for testing
  purposes. For production use, it is recommended to run an Elasticsearch cluster. Documentation is available for
  connecting ThamesThrive to an Elasticsearch cluster.

# How can I troubleshoot issues with ThamesThrive installation?

- For troubleshooting solutions during ThamesThrive installation, you can refer to the provided documentation section on
  troubleshooting.

# Can I run ThamesThrive without starting the Redis instance?

- No.

# Can I use ThamesThrive with an existing Elasticsearch instance?

- Yes, you can connect ThamesThrive to an existing Elasticsearch instance. Documentation is available for connecting
  ThamesThrive to Elasticsearch via SSL.

# How can I access the ThamesThrive API documentation?

- The ThamesThrive API documentation can be accessed by visiting the provided URL.

# How can I access the local copy of the ThamesThrive documentation?

- The local copy of the ThamesThrive documentation can be accessed by visiting the provided URL. Make sure the documentation
  Docker is started.

# Can I access ThamesThrive API and GUI from different IP addresses?

- Yes, you can access the ThamesThrive API and GUI from different IP addresses by replacing "localhost" with the appropriate
  IP in the configuration.

# Can I specify a different version for the ThamesThrive worker?

- Yes, you can specify a different version for the ThamesThrive worker by adding a version tag to the Docker image name in
  the command, such as `ThamesThrive/update-worker:<version>`. Make sure to keep the worker version the same as the ThamesThrive
  API version.

# What are the software prerequisites for installing ThamesThrive from source?

The software prerequisites for installing ThamesThrive from source are:

- Docker
- Python version 3.9 or 3.10 (for version 0.8.1+)
- Pip
- Python Virtual Environment
- PyCharm
- Git

# What are the options for launching Elasticsearch on Ubuntu?

There are two options for launching Elasticsearch on Ubuntu:

1. Installing Elasticsearch as a service
2. Installing Elasticsearch as a Docker container

# How can I install Elasticsearch as a service on Ubuntu?

To install Elasticsearch as a service on Ubuntu, follow these steps:

- Import the Elasticsearch public GPG key using cURL and add the Elastic package source list.
- Update the package lists and install Elasticsearch using APT.

# How can I install Elasticsearch as a Docker container on Ubuntu?

To install Elasticsearch as a Docker container on Ubuntu, use the following command:

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.2
```

# How do I download the ThamesThrive source code?

To download the ThamesThrive source code, use the following commands:

```
git clone https://github.com/ThamesThrive/ThamesThrive
git clone https://github.com/ThamesThrive/ThamesThrive-api
```

# How do I create virtual environments for ThamesThrive source?

To create virtual environments for ThamesThrive, follow these steps:

- Navigate to the respective directory (`ThamesThrive-api` or `ThamesThrive`).
- Use the `python3.9 -m venv venv` command to create a virtual environment.

# How do I install the dependencies for ThamesThrive when installing form source?

The installation steps for dependencies vary depending on the operating system:

### Linux

```
cd ThamesThrive-api
source venv/bin/activate
pip3 install wheel
pip install -r app/requirements.txt
```

### Windows

```
cd ThamesThrive-api
venv\Scripts\activate
pip install -r app/requirements.txt
```

### Mac OS

```
cd ThamesThrive-api
source venv/bin/activate
pip install -r app/requirements.txt
```

# How can I test access to the ThamesThrive documentation?

To test access to the ThamesThrive documentation, visit http://0.0.0.0:8686/docs.
