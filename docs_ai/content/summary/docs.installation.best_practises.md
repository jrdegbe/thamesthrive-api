The documentation provided outlines best practices for setting up and using the ThamesThrive API. It is recommended to set
up an encrypted connection when accessing the API, either by encoding the traffic as it is sent to the load balancer or
by preparing HTTPS versions of the ThamesThrive Docker images. It is also recommended to have two separate ThamesThrive API
clusters, one for GUI and one for event collection, with the event collecting cluster having the environment
variable `EXPOSE_GUI_API` set to `no`. Finally, the documentation provides information on how to scale the ThamesThrive
cluster, recommending the use of Kubernetes as a container orchestration platform.
