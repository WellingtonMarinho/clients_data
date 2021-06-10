

## Build and run docker image:
    $ docker compose build
    $ docker network create network_local
    $ docker compose up

### For run Django commands:
    $ docker container exec -ti django_app python manage.py [command]

### For run console on to container:
    $ docker container exec -ti django_app /bin/bash