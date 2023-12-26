# Open-Source Installation

Welcome to the installation documentation for the open-source version of ThamesThrive. This guide will walk you through the
process of installing ThamesThrive, which consists of three main components: API, GUI, and Update Worker.

## Docker compose installation

The simplest approach to installing ThamesThrive is by using Docker Compose. It's important to note that this installation
is intended for testing purposes only, as it doesn't configure the database and Redis properly.

1. **[Installation via docker compose](../docker-compose/opensource.md):** One liner installation for testing purposes.

## Docker one-by-one installation

The installation of open-source version of ThamesThrive has the following steps:

1. **[API Installation](../docker/ThamesThrive_with_docker.md#start-ThamesThrive-api):** The API component serves as the
   interface through which various interactions with the ThamesThrive system.

2. **[GUI Installation](../docker/ThamesThrive_with_docker.md#start-ThamesThrive-gui):** The GUI (Graphical User Interface) is
   the visual representation of the ThamesThrive system.

3. **[Update Worker Installation](../workers/install_update_worker.md):** The Update Worker is a part of the ThamesThrive
   system responsible for handling updates, patches, and maintenance tasks.

