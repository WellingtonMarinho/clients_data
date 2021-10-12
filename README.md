

## Build and run docker image:
    $ docker compose build
    $ docker network create data_local
    $ docker compose up

### Add file bin/.bash in path postactivate for charge alias:
    docker-build
    docker-up
    docker-manage
    docker-bash

### For run Django commands:
    $ docker container exec -ti django_app python manage.py [command]

### For run populate database
    $ docker container exec -ti django_app python manage.py populate
    $ docker container exec -ti django_app python manage.py populate_in_elasticsearch

### For clear and reindexing documents in elasticsearch
    $ docker container exec -ti django_app python manage.py search -c

### For run console on to container:
    $ docker container exec -ti django_app /bin/bash

#### Update docker image in heroku server
    $ heroku container:release web