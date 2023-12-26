# SSL Configuration

You have several options to run ThamesThrive in SSL mode.

## Building ThamesThrive API with SSL certificates embedded into docker

Clone repository `ThamesThrive/ThamesThrive-api.git`.

```
git clone https://github.com/ThamesThrive/ThamesThrive-api.git
```

Next go to ThamesThrive folder and find file **Dockerfile.ssl-internal** and type path to your SSL certificate and key file. 

* Find and replace `ssl/key.pem` with a path to your key file
* Find and replace `ssl/cert.pem` with a path to your certificate

This is how the **Dockerfile.ssl-internal** looks like

```
FROM tiangolo/uvicorn-gunicorn-fastapi

RUN apt-get update
RUN apt-get install -y git

# set the working directory in the container
RUN mkdir app/
WORKDIR /app

## Install dependencies
COPY app/requirements.txt .
RUN pip install -r requirements.txt

## Copy application
COPY app app/
COPY ssl ssl/
COPY docs manual/
ENV VARIABLE_NAME="application"

EXPOSE 443
CMD ["gunicorn", "-b", "0.0.0.0:443", "--workers", "25,"--keyfile", "ssl/key.pem", "--certfile", "ssl/cert.pem", "-k", "uvicorn.workers.UvicornWorker", "app.main:application"]
```

If you would like to tweak the number of workers running change `--workers` option in `gunicorn`.

Then run

```
cd ThamesThrive-api/
docker build . -f Dockerfile.ssl-internal -t ThamesThrive-api-ssl
```

Once built you can run ThamesThrive with the following command:

```
docker run -p 8686:443 -e ELASTIC_HOST=http://<your-laptop-ip>:9200 ThamesThrive-api-ssl
```

This will make API available at __https://localhost:8686__. If you want it on the standard HTTPS port run:

```
docker run -p 443:443 -e ELASTIC_HOST=http://<your-laptop-ip>:9200 ThamesThrive-api-ssl
```

And the API will be available __https://localhost__.

## Running ThamesThrive API with SSL certificates provided from outside container

Sometimes you do not want to build the docker yourself. Then you can use the prebuilt docker and attach
your certificates. To do that pull `ThamesThrive/ThamesThrive-api-ssl`.

```
docker pull ThamesThrive/ThamesThrive-api-ssl
```

Then copy your SSL certificates to any folder. For the purpose of this manual we place it in `/local/path/to/ssl`.
You can place it anywhere but remember to change the location in the command below:

```
docker run \
-v /local/path/to/ssl:/ssl \
-p 8686:443 \
-e ELASTIC_HOST=http://<your-elastic-instance-ip>:9200 \
-e GUNICORN_CMD_ARGS="--keyfile=/ssl/key.pem --certfile=/ssl/cert.pem" \
ThamesThrive/ThamesThrive-api-ssl
```

It will start ThamesThrive with files from your local `/local/path/to/ssl` folder copied/linked to internal docker folder called `/ssl`.
If you placed certificates inside that folder then the files will be accessible form `/ssl` in docker.
The Docker image expects na SSL key file to be named `key.pem` and certificate to be named `cert.pem`.

## ThamesThrive API behind HTTPS proxy

You can use treafik to hide ThamesThrive API behind HTTPS proxy.

Refer to this link for instructions:
https://traefik.io/resources/traefik-fastapi-kuberrnetes-ai-ml/

## ThamesThrive GUI in HTTPS mode

```
git clone https://github.com/ThamesThrive/ThamesThrive-gui.git
```

Find `ThamesThrive-gui/nginix/conf-ssl/certs` and place there your certificates:

* cert.pem
* key.pem

Run

```
docker build . -f Dockerfile-https --no-cache -t ThamesThrive/ThamesThrive-gui-https
```

Use `ThamesThrive/ThamesThrive-gui-https` as you docker image instead of `ThamesThrive/ThamesThrive-gui`.

