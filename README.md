|             | status |
|-------------|------------|
| **master** | [![Build Status](https://travis-ci.org/afourmy/flask-gentelella.svg?branch=master)](https://travis-ci.org/afourmy/flask-gentelella) [![Coverage Status](https://coveralls.io/repos/github/afourmy/flask-gentelella/badge.svg?branch=master)](https://coveralls.io/github/afourmy/flask-gentelella?branch=master)
| **develop** | [![Build Status](https://travis-ci.org/afourmy/flask-gentelella.svg?branch=develop)](https://travis-ci.org/afourmy/flask-gentelella) [![Coverage Status](https://coveralls.io/repos/github/afourmy/flask-gentelella/badge.svg?branch=develop)](https://coveralls.io/github/afourmy/flask-gentelella?branch=develop)

# Flask Gentelella

_Special thanks to the original content creators and developers of [Gentelella](https://github.com/puikinsh/gentelella) for this beautiful template._

![Gentelella Bootstrap Admin Template](https://cdn.colorlib.com/wp/wp-content/uploads/sites/2/gentelella-admin-template-preview.jpg "Gentelella Theme Browser Preview")

This project integrates Gentelella with Flask using: 
- [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for scalability.
- [flask_login](https://flask-login.readthedocs.io/en/latest/) for the login system (passwords hashed with bcrypt).
- [GraphQL](https://github.com/graphql-python/graphene) for data optimization.
- [mongoDB](https://github.com/mongodb/mongo) for data storage.

Flask-gentelella also comes with a robust CI/CD pipeline using:
- [Pytest](https://docs.pytest.org/en/latest/) framework for the test suite (see the `tests` folder).
- [Travis CI](https://travis-ci.org/afourmy/flask-gentelella) for automated test units.
- [Coverage](https://coveralls.io/github/afourmy/flask-gentelella) to measure the code coverage of the tests.
- [Selenium](https://www.seleniumhq.org/) to test the application with headless chromium.
- A Dockerfile showing how to containerize the application with gunicorn, and a [Docker image](https://hub.docker.com/r/afourmy/flask-gentelella/) available on dockerhub, and integrated to the CI/CD pipeline (see instructions below).


# Installation

### (Optional) Set up a [virtual environment](https://docs.python.org/3/library/venv.html) 

### 1. Get the code
    git clone https://github.com/afourmy/flask-gentelella.git
    cd flask-gentelella

### 2. Install requirements 
    pip install -r requirements.txt

### 3. Set the FLASK_APP environment variable
    (Windows) set FLASK_APP=gentelella.py
    (Unix) export FLASK_APP=gentelella.py

### 4. Run the application
    flask run --host=0.0.0.0

### 4. Go the http://127.0.0.1:5000/index

### 5. Create an account and log in


# Run Flask Gentelella in a docker container in one command

### 1. Fetch the image on dockerhub
    docker run -d -p 5000:5000 --name gentelella --restart always afourmy/flask-gentelella

### 2. Go the http://127.0.0.1:5000/index


