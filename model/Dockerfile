FROM python:3.8.3-alpine

ADD . /home/app/
WORKDIR /app


ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000


CMD [ "python3", "app.py" ]