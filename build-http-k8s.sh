git rev-parse HEAD > app/tracker/revision.txt
docker build . --rm -f docker.k8s.Dockerfile -t ThamesThrive/ThamesThrive-api-k8s:0.8.1
docker push ThamesThrive/ThamesThrive-api-k8s:0.8.1
