# Elastic search authentication

When preparing on you production installation you may need to authenticate to 
elastic search.

We provide different types of elastic search authentication. If you experience 
Authentication Error please take a closer look at the ThamesThrive configuration. 
You probably need to provide a username and password for an elastic-search 
connection. 


## Basic Authentication

Example of elastic search URI for authenticated access.


#### Encrypted authentication

File docker-standalone.yaml
```yaml
  ThamesThrive:
    build: .
    environment:
      ELASTIC_HOST: https://user:name@elastic-search-ip:443  <- change here for ssl connection
    ports:
      - 80:80  
    depends_on:
      - elasticsearch
```

#### Unencrypted authentication

For unencrypted connection set ELASTIC_HOST in docker-standalone.yaml to:

```yaml
  ThamesThrive:
    ...
    environment:
      ELASTIC_HOST: user:name@elastic-search-ip:9200
    ...
```

If you still experience problems with connection to elastic search, you can find the section on how to configure a connection to elastic search cluster below. 
