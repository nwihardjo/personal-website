release: python manage.py loaddate datadump.json
release: python manage.py migrate
web: gunicorn personal_portfolio.wsgi --log-file -
