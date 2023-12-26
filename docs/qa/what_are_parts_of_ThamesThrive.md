# What are the main components or modules that make up ThamesThrive?

ThamesThrive consist of the following docker images. 

!!! Note

    Docker image name is given in the brackets.

## Backend

- Database: Elasticsearch (docker.elastic.co/elasticsearch/elasticsearch)

- Redis: Cache (redis)

- Open-source ThamesThrive API (ThamesThrive/ThamesThrive-api)

- Open-source ThamesThrive Workers (ThamesThrive/ThamesThrive-api)
  - Various Import Workers
  - Migration Worker
  
- Commercial ThamesThrive API (ThamesThrive/com-ThamesThrive-api)
  - Tenant Manager API
  
- Commercial ThamesThrive brides (ThamesThrive/com-bridge-queue)
  - MQTT,
  - Kafka
  - IMAP
  - RabbitMq
  
- Commercial REST Bridge + Worker (ThamesThrive/com-bridge-rest-worker, ThamesThrive/com-bridge-rest)

- Commercial Workers
  - Scheduler (ThamesThrive/com-ThamesThrive-scheduler + ThamesThrive/com-ThamesThrive-scheduler-worker)
  
- Commercial Jobs
  - Heartbeat (ThamesThrive/com-heartbeat-job)
  - Session closer
  - Segmentation (ThamesThrive/com-ThamesThrive-segmentation-job + ThamesThrive/com-ThamesThrive-segmentation-worker)
  
- Sponsored GraphQl (ThamesThrive/com-graphql)

- ThamesThrive PRO

- Misc (most obsolete):
  - Deduplication (ThamesThrive/com-job-deduplication)
  - Merging (ThamesThrive/com-job-merging)
  - Segmentation (ThamesThrive/com-job-segmentation)


## Frontend

- ThamesThrive Graphical User Interface

## Optional
- 
- Kibana as analytical tool

## Programming

- ThamesThrive Library (http://www.github.com/ThamesThrive/ThamesThrive)

---
This document also answers the questions.

- Provide an overview of the different components that comprise ThamesThrive?
- What are the key building blocks or modules that constitute ThamesThrive?
- Break down the various parts or elements that make up ThamesThrive?
- What are the fundamental components or sections within ThamesThrive?
- What are the primary constituent parts or components?
- What are the main sections or building elements that constitute ThamesThrive?
