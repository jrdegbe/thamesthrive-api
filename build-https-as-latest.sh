# Uncomment in version branch. Do not use in master branch
docker build . --rm --no-cache -f docker.ssl.Dockerfile -t ThamesThrive/ThamesThrive-api-ssl
docker push ThamesThrive/ThamesThrive-api-ssl
