# Ticket

## Build Instructions

1. create .env file using .env-example file.

```
cp .env.example .env
```

```
# Django
DEBUG=True
SECRET_KEY=django-insecure-(e(g7-507%!m45eaho7xiok$y73fmk33ud74w*a=emwc+(80ws
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=http://localhost:8000

# DB
POSTGRES_DB=ticketly
POSTGRES_USER=ticketly
POSTGRES_PASSWORD=ticketly
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

2. Run command for install e configure development environment.

```bash
make setup
```

3. Run command for execute project. open in you browser http://localhost:8000/ and http://localhost:5173/.

```bash
make run
```

4. make login using credentials created in make setup command.

```
user: dev
password: ticketly@#2025
```

When your avaliation is finish, then run command for kill all container.

## Interesting Commands

When your avaliation is finish, then run command for kill all container.

```bash
make stop
```

Command for update database executing makemigrations and migrate.

```bash
make dbupdate
```

Command for execute just makemigrations.

```bash
make makemigrations
```

Command for execute just migrate.

```bash
make migrate
```

Command for clean dev environment fully.

```bash
make clean
```

## 📦 Tecnologias

- Python 3.13+
- Django 5.2
- Django REST Framework
- DRF Spectacular (Swagger)
- Python Decouple
- Docker