### Run tests
For running tests from outside

``docker compose run -e DJANGO_SETTINGS_MODULE=configuration.testing --rm web python3 manage.py test``