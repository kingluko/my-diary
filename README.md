# My- Diary
This is an Andela Bootcamp Challenge that provides a platform in which users can pen down their thoughts and feelings
# Contains
This project contains the following endpoints for the API
| Endpoint | **Functionality** |
| ------ | ------ |
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
Create Database on postgresql<br>
`- psql -c 'CREATE DATABASE "my-diary";' -U postgres`<br>
Create a user to access the database <br>
`- psql -c "CREATE USER kelvin WITH PASSWORD 'spongebob' createdb;" -U postgres`<br>
Create tables for the database<br>
`python database.py`<br>
Run the program<br>
`python run.py`<br>
View on postman<br>
`http://127.0.0.1/api/v1/<endpoint>`
