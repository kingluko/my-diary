# My-Diary V1

This is an Andela Bootcamp Challenge that provides a platform in which users can pen down their thoughts and feelings.

[![Build Status](https://travis-ci.org/kingluko/my-diary.svg?branch=develop)](https://travis-ci.org/kingluko/my-diary) [![Coverage Status](https://coveralls.io/repos/github/kingluko/my-diary/badge.svg?branch=ft-add-entry-159058043)](https://coveralls.io/github/kingluko/my-diary?branch=ft-add-entry-159058043) [![Maintainability](https://api.codeclimate.com/v1/badges/e073f9d3ab40ba7fcd93/maintainability)](https://codeclimate.com/github/kingluko/my-diary/maintainability)
# Contains
This application contains the following endpoints for the API

| Endpoint | **Functionality** |
| ------ | ------ |
| **GET /entries** | Fetch all entries |
| **GET /entries/<entryId>** | Fetch a single entry |
|**POST /entries**| Create an entry |
| **PUT /entries/<entryId>** | Modify an entry |

# Prerequisites
- Python3 (A programming language)
- Flask (A Python microframework)
- Virtualenv (Stores all dependencies used in the project)
- Pivotal Tracker (A project management tool)
- Pytest (Tool for testing)

# Installing
**Clone the repository**
 git clone https://github.com/kingluko/my-diary.git
**Create a virtual environment to install the dependencies**
 virtualenv --python=python3 yourenvname
**Install requirements within the virtual environment**
pip install -r requirements.txt
**Running the program**
 python run.py

# Live App on heroku
https://my-diary-kelvin.herokuapp.com/api/v1/entries

