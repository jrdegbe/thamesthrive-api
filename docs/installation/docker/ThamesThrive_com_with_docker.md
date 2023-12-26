# Docker-based ThamesThrive Installation

Make sure you have docker installed on your system.

## ThamesThrive API Version

!!! Note

    The following instalation description use the latest ThamesThrive container version. If you would like to install stable version 
    of the system, what we strongly recommend, please add to `tracard/com-ThamesThrive-api` a tag with version, e.g `ThamesThrive/com-ThamesThrive-api:0.8.1`. 
    The same applies to `ThamesThrive/ThamesThrive-gui`. Keep the version of API and GUI the same. 

## Access to commercial dockers

When you buy a ThamesThrive license, you'll get a DockerHub token. This token lets you download the commercial dockers.

ThamesThrive GUI looks the same in both the open-source and commercial versions. The only difference is the API.

### Login to Docker Hub

```bash
docker login -u tracari -p <token>
```

### Set the LICENSE

Then create a file .env-docker and paste the LICENSE in it:

```
API_LICENSE="paste license here"
```

When running linux:

```
set -a
source .env-docker
```

### Start ThamesThrive API

Pull and run ThamesThrive backend.

```bash
docker run -p 8686:80 -e ELASTIC_HOST=http://<your-elastic-ip>:9200 -e REDIS_HOST=redis://<your-redis-ip>:6379 ThamesThrive/com-ThamesThrive-api #(1)
```

1. Replace <your-elastic-ip> with your elastic IP. Do the same with <your-redis-ip>

ThamesThrive must connect to elasticsearch. To do that you have to set ELASTIC_HOST variable to reference your elasticsearch
instance.

!!! Warning "Waiting for application startup"

    Notice that when type `http://localhost:9200` you try to connect to Elastic on localhost. This means that you're
    connecting to the docker itself as localhost means local in docker. Obviously elastic is not there, so ThamesThrive will
    never connect. Pass external ip for elastic. This may be your laptop IP if you are running ThamesThrive locally.

For more troubleshooting solutions go to [Troubleshooting](../../trouble/index.md)

!!! More

    For more elasticseach connection types, e.g. via HTTP see [advanced elasticsearch connection](../../configuration/elasticsearch/elastic_https.md).

### API Documentation

For API documentation visit http://127.0.0.1:8686/docs

## Start ThamesThrive GUI

Pull and run ThamesThrive Graphical User Interface.

```bash
docker run -p 8787:80 ThamesThrive/ThamesThrive-gui #(1)
```

1. If you want a certain version of docker image add version tag, e.g. `ThamesThrive/ThamesThrive-gui:0.8.1`

## Run ThamesThrive Graphical User Interface

Visit http://127.0.0.1:8787 and follow the instructions to finish up the ThamesThrive set-up. When asked for ThamesThrive API
type: http://127.0.0.1:8686. 
