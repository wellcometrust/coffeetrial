#!/bin/sh
python3 manage.py recreate-db;
python3 manage.py new-round;

if [ "$FLASK_ENV" = "development" ]; then
    python3 manage.py run -h0.0.0.0;
else
    gunicorn -b 0.0.0.0:5000 manage:app
fi

exit 0
