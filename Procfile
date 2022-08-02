web: gunicorn my_site.wsgi --log-file -
worker: celery -A my_site worker -l info --pool=solo
