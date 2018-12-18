# Use a basic Python image
FROM python:3.6.4-slim-stretch

WORKDIR /rct

ENV APP_SETTINGS=config.ProductionConfig

COPY ./admin/matches.py /rct/admin/matches.py
COPY ./admin/round.py /rct/admin/round.py
COPY ./admin/user.py /rct/admin/user.py

COPY ./client/matching.py /rct/client/matching.py

COPY ./manage.py /rct/manage.py
COPY ./models.py /rct/models.py
COPY ./app.py /rct/app.py
COPY ./config.py /rct/config.py


COPY ./requirements.txt /rct/requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "run"]
