alias docker-build='docker compose build --no-cache'
alias docker-up='docker compose up'
alias docker-manage='docker container exec -ti django_app python manage.py $@'
alias docker-bash='docker container exec -ti django_app /bin/bash'