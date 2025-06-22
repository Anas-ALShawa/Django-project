web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn myfinal.wsgi:application --host 0.0.0.0 --port $PORT
