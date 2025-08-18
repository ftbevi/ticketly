ARGS = $(filter-out $@,$(MAKECMDGOALS))

COMPOSE_COMMAND=$(shell command -v docker-compose >/dev/null 2>&1 && echo "docker-compose" || echo "docker compose")

build:
	$(COMPOSE_COMMAND) build

clean:
	$(COMPOSE_COMMAND) kill && $(COMPOSE_COMMAND) down --rmi all
	docker volume prune
	sudo rm -rf resources/

createsuperuser:
	$(COMPOSE_COMMAND) run server python manage.py shell -c "from apps.accounts.models import User; \
	u, _ = User.objects.get_or_create(email='dev@ticketly.co'); \
	u.username = 'dev'; \
	u.set_password('ticketly@#2025'); \
	u.is_superuser = u.is_staff = True; \
	u.save(); \
	print('Superuser: dev / ticketly@#2025');"

statics:
	$(COMPOSE_COMMAND) run --rm server python manage.py collectstatic --noinput

migrate:
	$(COMPOSE_COMMAND) run --rm server python manage.py migrate

migrations:
	$(COMPOSE_COMMAND) run --rm server python manage.py makemigrations

dbupdate: migrations migrate

services:
	$(COMPOSE_COMMAND) up -d db
	$(COMPOSE_COMMAND) up -d mail

setup: build services dbupdate createsuperuser statics

bash:
	$(COMPOSE_COMMAND) run --rm $(ARGS) sh

stop:
	$(COMPOSE_COMMAND) down --remove-orphans

run:
	$(COMPOSE_COMMAND) up -d server
	$(COMPOSE_COMMAND) up -d web