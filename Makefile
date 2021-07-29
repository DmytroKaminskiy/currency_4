SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

makemigrations:
	$(manage_py) makemigrations

worker:
	cd app && celery -A settings worker -l info

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

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
