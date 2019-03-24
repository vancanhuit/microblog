FROM python:3.7-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN pip install -U pip setuptools
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY main.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP main

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000

ENTRYPOINT [ "./boot.sh" ]
