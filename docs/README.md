# Install
```
pip install -r docs/requirements.txt 
```


# Test
run in ThamesThrive-api
```
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

# Build
Type `mkdocs build` in folder / in ThamesThrive-api (it must be single project, without attached ThamesThrive, etc.)
