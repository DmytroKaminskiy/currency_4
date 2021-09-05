SHELL := /bin/bash

manage_py := docker exec -it backend python ./app/manage.py

build:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

down:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

runserver:
	$(manage_py) runserver 0:8001

collectstatic:
	$(manage_py) collectstatic --noinput && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

makemigrations:
	$(manage_py) makemigrations

beat:
	cd app && celery -A settings beat -l info

migrate:
	$(manage_py) migrate

generate_data:
	$(manage_py) generate_data

createsuperuser:
	$(manage_py) createsuperuser

show_urls:
	$(manage_py) show_urls

shell:
	$(manage_py) shell_plus --print-sql

pytest:
	pytest app/tests/ --cov=app --cov-report html && coverage report --fail-under=71.3910

gunicorn:
	cd app && gunicorn -w 4 settings.wsgi:application -b 0.0.0.0:8001 --log-level=DEBUG

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
