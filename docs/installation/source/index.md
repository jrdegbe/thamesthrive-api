# Installation from source

## Software prerequisites

* Docker
* Python version 3.9 or 3.10 (for version 0.8.1+)
* Pip
* Python Virtual Environment
* PyCharm
* Git
* [Elasticsearch](../dependencies/elasticsearch.md)
* Redis

Install the above software, and we're ready to start.

# Download the source code

Open a terminal and go to the directory where you want to keep the code. Enter:

```bash
git clone https://github.com/ThamesThrive/ThamesThrive  #(1)
git clone https://github.com/ThamesThrive/ThamesThrive-api #(2)
```

1. Clones ThamesThrive repository. Code will be available in ThamesThrive folder.
2. Clones ThamesThrive-api repository

# Create virtual environments

Type:

```bash
cd ThamesThrive-api
python3.9 -m venv venv  # (1)
cd ..
cd ThamesThrive
python3.9 -m venv venv
```

1. Installs virtual environment with python 3.9 or 3.10 (for version 0.8.1+)

!!! Tip

    Before creating the virtual environment make sure you have version 3.9.x installed. Type `python --version` to see if the version is correct.

# Install dependencies

=== "Linux"

    ```bash
    # Activates virtual environment (1)
    cd ThamesThrive-api
    source venv/bin/activate

    # Install wheel
    pip3 install wheel
    
    # Installs dependencies
    pip install -r app/requirements.txt
    
    # Run code (2)
    USER_NAME=admin PASSWORD=admin uvicorn app.main:application --host 0.0.0.0 --port 8686
    ```

    1. Only ThamesThrive-api is required to run the API. ThamesThrive library will be installed as dependency.
    2. Sets default username: password as admin: admin and runs ThamesThrive API on port 8686.

=== "Windows"

    ```bash
    cd ThamesThrive-api
    venv\Scripts\activate
    
    // Installs dependencies
    pip install -r app/requirements.txt
    
    // Run code 
    USER_NAME=admin PASSWORD=admin uvicorn app.main:application --host 0.0.0.0 --port 8686
    ```

=== "Mac OS"

    ```bash
    // Activates virtual environment
    cd ThamesThrive-api
    source venv/bin/activate
    
    // Installs dependencies
    pip install -r app/requirements.txt
    
    // Run code
    USER_NAME=admin PASSWORD=admin uvicorn app.main:application --host 0.0.0.0 --port 8686
    ```

# Test access to documentation

Visit http://0.0.0.0:8686/docs


