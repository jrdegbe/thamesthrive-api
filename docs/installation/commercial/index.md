# Commercial Installation

This guide will provide step-by-step instructions for installing commercial ThamesThrive. Some aspects of this installation
process are quite similar to the open-source installation.

## Prerequisites

To set up Commercial ThamesThrive, you'll need access to DockerHub token and a valid commercial license key. This information will
be sent to you after purchase of the commercial license.

## Docker compose installation

The simplest approach to installing ThamesThrive is by using Docker Compose. It's important to note that this installation
is intended for testing purposes only, as it doesn't configure the database and Redis properly.

1. **[Installation via docker compose](../docker-compose/commercial.md):** One liner installation for testing purposes.

## Docker one-by-one installation

The installation of open-source version of ThamesThrive has the following steps:

1. **[API Installation](../docker/ThamesThrive_com_with_docker.md#start-ThamesThrive-api):** The API component serves as the
   interface through which various interactions with the ThamesThrive system.

2. **[GUI Installation](../docker/ThamesThrive_com_with_docker.md#start-ThamesThrive-gui):** The GUI (Graphical User Interface) is
   the visual representation of the ThamesThrive system.

3. **[Workers Installation](../workers/installation.md):** Workers are parts of the ThamesThrive
   system responsible for handling updates, segmentation, triggers, and maintenance tasks.

4. **[Jobs Installation](../jobs/index.md):** Jobs are parts of the ThamesThrive
   system responsible for triggering jobs for workers.

## Kubernetes' installation with helm


1. **[Installation with Helm on K8S](../production/k8s/helm.md):** Automates installation of all required ThamesThrive components.
