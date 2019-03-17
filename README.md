# Simple Microblog web application using Python 3 and Flask framework
[![Build Status](https://travis-ci.org/vancanhuit/microblog.svg?branch=develop)](https://travis-ci.org/vancanhuit/microblog)

Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Local development

- Activate a python virtual environment in your local machine:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -U pip
    pip install -r requirements.txt
    ```

- Clone this repository into local machine:
    ```sh
    git clone https://github.com/vancanhuit/microblog.git
    cd microblog
    ```

- Install [elasticsearch](https://www.elastic.co/downloads/elasticsearch), run it on your local machine and create `post` index:
    ```sh
    curl -X PUT "http://localhost:9200/post?pretty"
    ```

- Create `.env` file which contains necessary environment variables for running application with following contents:

    ```text
    FLASK_APP=main
    FLASK_ENV=development
    #FLASK_DEBUG=1

    MAIL_SERVER="smtp.gmail.com"
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME="<your-mail-address-username>"
    MAIL_PASSWORD="<your-mail-address-password>"
    ADMINS="<your-admin-emails-seperated-by-semicolon>"

    ELASTICSEARCH_URL="http://localhost:9200"
    ```

- Run the following command to initialize sqlite database:
    ```sh
    flask db init
    flask db upgrade
    ```
- Run flask app and open http://localhost:5000 on your web browser:
    ```sh
    flask run
    ```

## Resources
- [Flask framework](http://flask.pocoo.org/).
- [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html) and [Elasticsearch python client](https://elasticsearch-py.readthedocs.io/en/master/).
- [SQLAlchemy](https://docs.sqlalchemy.org/en/latest/) and [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org).
- [Heroku deployment](https://devcenter.heroku.com/categories/python-support).
- [Gunicorn](https://gunicorn.org/).
- [Psycopg](http://initd.org/psycopg/).
