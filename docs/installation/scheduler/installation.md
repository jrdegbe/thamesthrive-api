# Scheduler Installation

The Scheduler is an essential component of the commercial ThamesThrive platform. Certain functionalities within ThamesThrive,
such as the "Pause and Resume", or "Run In Background" plugin and any time-based triggers, rely on the Scheduler.

To successfully run the Scheduler, you will need to set up the following Docker containers:

* __ThamesThrive/com-ThamesThrive-scheduler-worker__: This container processes triggers.

## Starting the Docker Containers

Before starting the Docker containers, ensure that the container is configured in the same way as
ThamesThrive/ThamesThrive-api. If the API is set to run as a multi-tenant application, the Scheduler must also be configured
accordingly.

The Scheduler does not need to be explicitly set to PRODUCTION=yes or no. The production context is specified in the
task description, enabling the Scheduler to connect to the appropriate database.

If you do not set up the multi-tenancy correctly, you may encounter the following error: "invalid source."

Use the following example Docker command to start the worker container:

```bash
docker run \
-e ELASTIC_HOST=http://<es-host>:9200 \
-e REDIS_HOST=<redis-host> \
-e MULTI_TENANT_MANAGER_URL=http://<tms-host>:8080 \
-e MULTI_TENANT_MANAGER_API_KEY=123 \
-e MULTI_TENANT=yes \
ThamesThrive/com-ThamesThrive-scheduler-worker:0.8.1
```

For non-multi-tenant setups, use the following Docker command:

```bash
docker run \
-e ELASTIC_HOST=http://<es-host>:9200 \
-e REDIS_HOST=<redis-host> \
ThamesThrive/com-ThamesThrive-scheduler-worker:0.8.1
```

Please ensure that you replace the environment variable values (ELASTIC_HOST, REDIS_HOST, etc.) with the appropriate
configurations for your specific setup.
