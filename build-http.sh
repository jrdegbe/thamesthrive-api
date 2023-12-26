git rev-parse HEAD > app/tracker/revision.txt
docker build . --rm --no-cache -f docker.Dockerfile -t ThamesThrive/ThamesThrive-api:0.8.1
docker push ThamesThrive/ThamesThrive-api:0.8.1
