[![Build Status](https://travis-ci.org/kingluko/my-diary.svg?branch=Develop-API)](https://travis-ci.org/kingluko/my-diary) [![Coverage Status](https://coveralls.io/repos/github/kingluko/my-diary/badge.svg?branch=ch-travis-config-159386973)](https://coveralls.io/github/kingluko/my-diary?branch=ch-travis-config-159386973) [![Maintainability](https://api.codeclimate.com/v1/badges/e073f9d3ab40ba7fcd93/maintainability)](https://codeclimate.com/github/kingluko/my-diary/maintainability)
# My- Diary
This is an Andela Bootcamp Challenge that provides a platform in which users can pen down their thoughts and feelings
# Contains
This project contains the following endpoints for the API

| Endpoint | **Functionality** |

| **POST /auth/signup** | Create an account |

| **POST /auth/signin** | Login a user |

| **GET /entries** | Fetch all entries |

| **GET /entries/<entryId>** | Fetch a single entry |

|**POST /entries**| Create an entry |

| **PUT /entries/<entryId>** | Modify an entry |

| **DELETE /entries/<entryId>** | Delete and Entry|

# Prereqisites

- Python3 (A programming language)
- Flask (A Python microframework)
- Virtualenv (Stores all dependencies used in the project)
- Pivotal Tracker (A project management tool)
- Pytest (Tool for testing)
- Postresql (Database)

# Installation
Clone the repository<br>
`git clone https://github.com/kingluko/my-diary.git`<br>
Create a virtual environment<br>
`virtualenv --python=python3 yourenvname`<br>
Install the requirements within the virtual environment<br>
`pip install -r requirements.txt`<br>
Access Postgres via command prompt<br>
`sudo -i -u postgres`<br>
Create Database on postgresql<br>
`- psql -c 'CREATE DATABASE "my-diary";' -U postgres`<br>
Create a user to access the database <br>
`- psql -c "CREATE USER kelvin WITH PASSWORD 'spongebob' createdb;" -U postgres`<br>
Create tables for the database on python<br>
`python database.py`<br>
Run the program<br>
`python run.py`<br>
View on postman<br>
`http://127.0.0.1/api/v1/<endpoint>`

# Documentation
The documentation for the API can be accessed on:<br>
https://mydiaryapi1.docs.apiary.io/

# Heroku
The app is live on heroku with the link below:<br>`
`https://my-diary-v2.herokuapp.com/api/v1`
