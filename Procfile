release: python manage.py loaddata datadump.json
release: python manage.py migrate
web: gunicorn personal_portfolio.wsgi --log-file -
