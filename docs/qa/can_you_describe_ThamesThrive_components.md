# Can you describe ThamesThrive components?

This is technical documentation of source code and dockers.

## Commercial ThamesThrive API

- Source: com-ThamesThrive/com_ThamesThrive, ThamesThrive/ThamesThrive
- Github: https://github.com/ThamesThrive/com-ThamesThrive, https://github.com/ThamesThrive/ThamesThrive
- Docker: ThamesThrive/com-ThamesThrive-api
- Description: This is commercial ThamesThrive API responsible for collecting and processing events.

## Commercial Jobs

### Heartbeats

- Source: com-ThamesThrive/com_job/heartbeat
- Github: https://github.com/ThamesThrive/com-ThamesThrive
- Docker: ThamesThrive/com-heartbeat-job
- Description: This job is responsible for running some defined event on all profiles. 

### Live Segmentation

- Source: com-ThamesThrive/com_job/segmentation
- Github: https://github.com/ThamesThrive/com-ThamesThrive
- Docker: ThamesThrive/com-ThamesThrive-segmentation-job
- Description: Iterate over live segmentation flows and push to the segmentation:live queue a job for worker that
  segments the profile based on the live workflows.

## Commercial Workers

### Scheduler

- Source: None
- Github: https://github.com/ThamesThrive/com-ThamesThrive
- Docker: ThamesThrive/com-ThamesThrive-scheduler-worker, ThamesThrive/com-ThamesThrive-scheduler
- Description: background processes for Pause and Result actions. This is basically as rq worker and rqscheduler from RQ
  library.

### Segmentation and Coping

- Source: com-ThamesThrive/com_worker
- Github: https://github.com/ThamesThrive/com-ThamesThrive
- Docker: ThamesThrive/com-ThamesThrive-segmentation-worker
- Redis Queue Worker that monitors the following queues:
    - segmentation:live,
    - event_to_profile_coping:worker,
    - event_props_to_event_traits:worker
- Description:
    - event_props_to_event_traits:worker is responsible for background coping of historical event properties to traits.
    - event_to_profile_coping:worker is responsible for background event to profile coping
    - segmentation:live is responsible for warning live segmentations. It is triggered by segmentation job.

## Commercial bridges

- Source: com-bridge-queue
- Github: https://github.com/ThamesThrive/com-bridge-queue
- Description: Queue bridges.

## Open-source ThamesThrive API

- Source:ThamesThrive
- Github: https://github.com/ThamesThrive/ThamesThrive-api
- Description: This is open-source ThamesThrive API responsible for collecting and processing events.

## Open-source Workers

- Source:ThamesThrive/worker
- Github: https://github.com/ThamesThrive/ThamesThrive-api
- Description: This is open-source ThamesThrive worker responsible for imports and system migration. 

---
This document also answers the questions.

- Provide an overview of the different components that comprise ThamesThrive ?
- What are the key building blocks or modules that constitute ThamesThrive ?
- What are the fundamental components or sections within ThamesThrive ?
- What are the main functions of ThamesThrive components ?
- What containers ThamesThrive needs?
