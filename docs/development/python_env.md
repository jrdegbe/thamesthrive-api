# Python development environment

## Software prerequisites

* Docker
* Python version 3.9.x
* Pip
* Python Virtual Environment
* PyCharm
* Git

Install the above software and we're ready to start.

Docker is required to start ThamesThrive storage (Elasticsearch) and Redis.

## Launching Redis and Elasticsearch

Redis instance is required to start ThamesThrive.

### Redis instance

Start Redis with:

```
docker run -p 6379:6379 redis
```

### Elasticsearch instance

Elasticsearch is the database that ThamesThrive uses for storing data.

Open a new terminal and enter to start Elasticsearch:

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.2
``` 

When you want to stop Elasticsearch or redis, press CTRL+C in the terminal you started the docker containers.

!!! Tip

    If you want elasticsearch to run in the background, type: 
    `docker run -d -p 9200: 9200 -p 9300: 9300 -e "discovery.type = single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.2`

## Download the source code

Open a terminal and go to the directory where you want to keep the code. Enter:

```bash
git clone https://github.com/ThamesThrive/ThamesThrive  #(1)
git clone https://github.com/ThamesThrive/ThamesThrive-api #(2)
```

1. Clones ThamesThrive repository. Code will be available in ThamesThrive folder.
2. Clones ThamesThrive-api repository

## Create virtual environments

We need to create 2 virtual environments. Type:

```bash
cd ThamesThrive-api
python3.9 -m venv venv  # (1)
cd ..
cd ThamesThrive
python3.9 -m venv venv # (2)
```

1. Installs virtual environment with python 3.9 for ThamesThrive API
2. Installs virtual environment with python 3.9 for ThamesThrive library

!!! Tip

    Before creating the virtual environment make sure you have version 3.9.x installed. Type `python --version` to see the python version.

## Install dependencies

=== "Linux"

    ```bash
    # Activates virtual environment (1)
    cd ThamesThrive-api
    source venv/bin/activate
    
    # Installs dependencies
    pip install -r app/requirements.txt
    deactivate 

    cd ..
    
    cd ThamesThrive
    source venv/bin/activate
    
    # Installs dependencies (2)
    pip install -r ThamesThrive/requirements.txt
    deactivate
    ```

    1. Only ThamesThrive-api is required to run the API. ThamesThrive library will be installed as dependency.
    2. Installs dependencies of ThamesThrive API.

=== "Windows"

    ```bash
    cd ThamesThrive-api
    venv\\Scripts\\activate
    
    // Installs dependencies
    pip install -r app\\requirements.txt
    deactivate

    cd ..

    cd ThamesThrive
    venv\\Scripts\\activate
    
    // Installs dependencies
    pip install -r ThamesThrive\\requirements.txt
    deactivate

    ```

=== "Mac OS"

    ```bash
    # Activates virtual environment (1)
    cd ThamesThrive-api
    source venv/bin/activate
    
    # Installs dependencies
    pip install -r app/requirements.txt
    deactivate 

    cd ..
    
    cd ThamesThrive
    source venv/bin/activate
    
    # Installs dependencies (2)
    pip install -r ThamesThrive/requirements.txt
    deactivate
    ```

    1. Only ThamesThrive-api is required to run the API. ThamesThrive library will be installed as dependency.
    2. Installs dependencies of ThamesThrive API.

!!! Tip

    Before creating the virtual environment make sure you have version 3.9.x installed. Type `python --version` to 
    see the python version.

!!! Bug "Trouble shooting"

    If you see an error that some of the libraries can not be installed, this may mean that you do not have python 
    version 3.9.x installed in your virtual environment.

## Importing project into PyCharm

The API and ThamesThrive library are installed. Now it is time to open IDE and run it inside code editor. ThamesThrive API
depends on ThamesThrive library we will need to reference library inside ThamesThrive API project.

1. Open `PyCharm`
2. Click `File/Open`
3. Find and select `ThamesThrive-api` folder
4. Click open project in `new window`
5. In the right lower corner next to maser branch, select `<no-interpreter>`
6. Click `add interpreter` and select existing environment

Now it is time to open `ThamesThrive library` and reference it as dependency of `ThamesThrive-api`

1. Open `PyCharm`
2. Click `File/Open`
3. Find and select `ThamesThrive` folder
4. Click open project as `attach`

You should see something like this in your PyCharm editor.

![Attached project in PyCharm](../images/attached-project.png)

## Running inside PyCharm

1. Find folder `app` in `ThamesThrive-api`
2. Find file `main.py`
3. Right click on it and select `Run 'main.py'`

Now the ThamesThrive API is running. You should see the following logs:

```text
INFO:     Started server process [59653]
INFO:uvicorn.error:Started server process [59653]
INFO:     Waiting for application startup.
INFO:uvicorn.error:Waiting for application startup.
INFO:     Application startup complete.
INFO:uvicorn.error:Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8686 (Press CTRL+C to quit)
INFO:uvicorn.error:Uvicorn running on http://0.0.0.0:8686 (Press CTRL+C to quit)
```

!!! Bug "Trouble shooting"

    If your logs stop on `INFO:uvicorn.error:Waiting for application startup.` that means your elasticsearch 
    docker is not running. Run it and the API will resule after the database is ready.  

!!! Warning "Running inside PyCharm"

    Running API inside PyCharm has some pros and cons. Pros are that you can debug the execution of API. Cons are that 
    when you change the code you have to rerun the program. 
    If you want to auto reload the API run in terminal 
    
    ```bash
    uvicorn app.main:application --reload --host 0.0.0.0 --port 8686  #(1)
    ```

    1. Runs ThamesThrive API on port 8686 via uvicorn.

    The above command will run serveral copies (workers) of ThamesThrive API.

!!! Tip

    ```
    .../elasticsearch/connection/base.py:193: ElasticsearchDeprecationWarning: Elasticsearch built-in security features 
    are not enabled. Without authentication, your cluster could be accessible to anyone. See 
    https://www.elastic.co/guide/en/elasticsearch/reference/7.13/security-minimal-setup.html to enable security.
    ```

    This warining may appear when you connect to elasticsearch without credentials set-up. This is not an issue when 
    you run development version of ThamesThrive. 


## Wrap-up

Testing API can be via `http://localhost:8686/docs`. If you need to test API with GUI console run the following docker 
command:

```bash
docker run -p 8787:80 -e API_URL=//127.0.0.1:8787 ThamesThrive/ThamesThrive-gui:<version>
```

!!! Info

    1. Replace `<version>` with current development version, for example: `0.7.3-dev`. If you do not know the current development version 
       please contact us at: __office(at)ThamesThrive.com__ or on any social media: __http://twitter.com/ThamesThrive__, __http://www.youtube.com/@ThamesThrive__,
       or via __slack__ or __https://github.com/ThamesThrive/ThamesThrive__

GUI will be available at `http://localhost:8787`.
