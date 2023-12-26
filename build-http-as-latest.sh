# Uncomment in version branch. Do not use in master branch
git rev-parse HEAD > app/tracker/revision.txt
docker build . --rm --no-cache -f docker.Dockerfile -t ThamesThrive/ThamesThrive-api
docker push ThamesThrive/ThamesThrive-api
