

## Build and run docker image:
    $ docker compose build
    $ docker network create data_local
    $ docker compose up

### Add file bin/.bash in path postactivate for charge alias:
    docker-build
    docker-up
    docker-manage
    docker-manage populate_all_models
    docker-bash

### For run Django commands:
    $ docker container exec -ti django_app python manage.py [command]

### For run populate database
    $ docker container exec -ti django_app python manage.py populate
    $ docker container exec -ti django_app python manage.py populate_in_elasticsearch
    $ docker container exec -ti django_app python manage.py create_products
    $ docker container exec -ti django_app python manage.py create_orders

### For clear and reindexing documents in elasticsearch
    $ docker container exec -ti django_app python manage.py search -c

### For run console on to container:
    $ docker container exec -ti django_app /bin/bash

#### Update docker image in heroku server
    $ heroku container:release web


## Exemple how to create a virtualenv using virtual wrapper and other python version 
    $ mkvirtualenv -p ~/.pyenv/versions/3.10.4/bin/python3.10 -a `pwd` teste_env


### Activate Hot Reload with Ipython in shell_plus django extensions 
    in .ipython/profile_default create file ipython_config.py then add: 

    print("--------->>>>>>>> ENABLE AUTORELOAD <<<<<<<<<------------")
    
    c = get_config()
    c.InteractiveShellApp.exec_lines = []
    c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
    c.InteractiveShellApp.exec_lines.append('%autoreload 2')
