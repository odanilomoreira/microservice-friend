FROM python

ENV PYTHONBUFFERED 1

WORKDIR /app

RUN pip install flask flask-restful flask-cors flask-sqlalchemy flask-caching pika

COPY . /app

CMD python app.py