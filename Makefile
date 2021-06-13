SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

makemigrations:
	$(manage_py) makemigrations

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
