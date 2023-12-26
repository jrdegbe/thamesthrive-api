# How import data and fix an error of import pending?

## Introduction:

ThamesThrive utilizes import workers to process data imports in the background, and sometimes import workers may face errors
that lead to import pending issues. In this documentation, we will guide you through the steps to start an import worker
and resolve import pending errors.

### Step 1: Start ThamesThrive Worker

To start importing data, you need to start the ThamesThrive worker that will import data in the background. You can use the
following Docker command to start the worker:

```bash
docker run -e REDIS_HOST=redis://<redis-ip>:6379 ThamesThrive/worker-update
```

In this command, replace <redis-ip> with the IP address of the Redis server that ThamesThrive uses.

### Step 2: Verify that the Worker is Running

After running the above command, the import worker will start processing defined data imports, and you can verify that
the worker is running by checking the list of running Docker containers using the following command:

```
docker ps
```

If the worker is not running, check the logs for any errors.

### Step 3: Check Background Tasks

After starting the worker, check the background tasks in ThamesThrive to ensure that the import worker has started
processing the import task. If the import worker did not start processing the task, try creating a new background task.

### Step 4: Troubleshoot Errors

If you encounter any errors during the import process, refer to the ThamesThrive documentation or seek help from the 
ThamesThrive community. Common issues that you may encounter include connection errors, malformed data, or unsupported 
file formats.
