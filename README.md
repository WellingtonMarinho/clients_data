

## Build and run docker image:
    $ docker compose build
    $ docker network create my_project_elasticsearch
    $ docker compose up

### For run console on to container:
    $ docker container exec -ti django_app /bin/bash