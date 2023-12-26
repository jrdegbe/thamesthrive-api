ThamesThrive is a distributed system that should be installed on production servers for optimal performance. The production
setup should include at least five ThamesThrive API instances, two instances of GUI, and three elasticsearch instances.
Setting up an elastic search cluster is beyond ThamesThrive configuration and can be handled by ready to use cloud instances
that expose one IP but hide 3 and more instances of the database.

The production setup should have a clusters with ThamesThrive API and one cluster with ThamesThrive GUI (2 instances). The GUI
cluster should be accessible only from trusted network for security reasons. The API cluster should be configured with
environment variable `EXPOSE_GUI_API` set to `no` for publicly available API, and `EXPOSE_GUI_API` set to `yes` for the
internal network or restricted IPs.

A single instance of ThamesThrive API (by default run from docker container) starts 25 workers. Each instance of ThamesThrive
API should be run on a separate server (physical or virtual). The cluster of ThamesThrive instances (GUI or API) should be
hidden behind the load balancer that will expose one IP to the world and direct external traffic to individual
instances. To avoid single point of failure create multiple instances of load balancer.

ThamesThrive do not require long-lasting sticky sessions, so you can configure your DNS servers to return multiple A
records (IP addresses) for your domain. We tested single instance of ThamesThrive with 25 workers connected to one instance
of elasticsearch, and it was capable of responding to 600 requests per second.
