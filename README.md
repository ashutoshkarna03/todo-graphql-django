# To-Do App
## A simple app to list out and manage all your todo tasks

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A simple GraphQL based TODO app where users can create their account and then create, list out and manage their todo task. Very simple and very easy to use application, useful for keeping track of your day-to-day tasks.

#### Contains two main modules
- User Module: Manage user creation and user authentication
- TODO Module: Manage the todo tasks creation, update, delete and list out (CRUD operations     on TODO tasks)

## Features

- Developed using Powerful Django, MongoDB and GraphQL
- Simple, fast, secured and easy to use application
- User Management and User Authentication 
- Create a todo task (if you are logged in user)
- Modify the existing TODO task (change name of task, mark it done, etc)
- Delete the exisitng task
- List out all the task
- Very flexible GraphQL APIs
- Can be hosted easily in cloud



## Tech

Dillinger uses a number of open source projects to work properly:

- [Django] - Powerful Python Based Web Framework
- [MongoDB] - NoSQL based Database
- [GraphQL] - a query language for APIs and a runtime for fulfilling those queries with your existing data
- [Docker] - containerization tool


## Installation

TODO App requires [Python](https://python.org/) v3.5+ to run.

Install MongoDB using Docker (Docker and Docker Compose needs to be installed first)
```sh
cd todo-graphql-django/mongodb
docker-compose up -d
```

Clone the repository first and then
```sh
cd todo-graphql-django
# install requirements/libraries
pip install -r requirements.txt
# perform migration
python manage.py migrate
# run project
python manage.py runserver
```

## API Docs
#### User APIs:

###### User List API
Path: /users
Request: 
```
{
  users {
    username
    email
    password
  }
}
```
response:
```
{
  "data": {
    "users": [
      {
        "username": "admin",
        "email": "admin@admin.com",
        "password": "pbkdf2_sha256$260000$fXt23mIu2GLATY7KM55BY8$+dJGUxOvT8Gz9q89IRrWLRenrB9E8GVSiBWd/60R1PE="
      },
      {
        "username": "Ashutosh",
        "email": "ashutosh@amil.com",
        "password": "pbkdf2_sha256$260000$7COgKL7tjq5JtT1oMuIFQP$pTbBWS9W9rte64MJFbZu2yAjRD4Er9XbaZTcITgtUek="
      }
    ]
  }
}
```
###### Create User API
Path: /users
Request: 
```
mutation {
  create_user: createUser (username:"Ashutosh", email:"ashutosh@amil.com", password:"hello") {
    user {
      username
      email
      password
    }
  }
}
```
response:
```
{
  "data": {
    "create_user": {
      "user": {
        "username": "Ashutosh",
        "email": "ashutosh@amil.com",
        "password": "pbkdf2_sha256$260000$7COgKL7tjq5JtT1oMuIFQP$pTbBWS9W9rte64MJFbZu2yAjRD4Er9XbaZTcITgtUek="
      }
    }
  }
}
```
###### Get Auth Token
Path: /users
Request: 
```
mutation {
  tokenAuth (username: "Ashutosh", password: "hello") {
    token
  }
}
```
response:
```
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkFzaHV0b3NoIiwiZXhwIjoxNjI5OTYyMjE5LCJvcmlnSWF0IjoxNjI5OTYxOTE5fQ.aI_UmiDcSPpu2ANg41RuhwyqhS49pe3aA7P1lxXfxlg"
    }
  }
}
```
###### Verify Auth Token
Path: /users
Request: 
```
mutation {
  verifyToken (token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkFzaHV0b3NoIiwiZXhwIjoxNjI5OTYyMjE5LCJvcmlnSWF0IjoxNjI5OTYxOTE5fQ.aI_UmiDcSPpu2ANg41RuhwyqhS49pe3aA7P1lxXfxlg") {
    payload
  }
}
```
response:
```
{
  "data": {
    "verifyToken": {
      "payload": {
        "username": "Ashutosh",
        "exp": 1629962219,
        "origIat": 1629961919
      }
    }
  }
}
```

#### TODO List APIs:

###### Get TODO List API
Path: /todo
Request: 
```
{
  toDoList {
    task
    isComplete,
    dateCreated
    id
  }
}
```
Response:
```
{
  "data": {
    "toDoList": [
      {
        "task": "Hello",
        "isComplete": false,
        "dateCreated": "2021-08-26T00:00:00+00:00",
        "id": "1"
      },
      {
        "task": "Demo Task 2",
        "isComplete": false,
        "dateCreated": "2021-08-26T00:00:00+00:00",
        "id": "2"
      }]
    }
}
```
###### Create TODO Task API
Path: /todo
Request: 
```
mutation {
  create_todo_list: createTodoList(task: "Hello Trial Final", createdBy: 1, isComplete: true) {
    toDo {
      task
      createdBy
      isComplete
      id
    }
  }
}
```
Response:
```
{
  "data": {
    "create_todo_list": {
      "toDo": {
        "task": "Hello Trial Final",
        "createdBy": 1,
        "isComplete": true,
        "id": "18"
      }
    }
  }
}
```
###### Update TODO Task API
Path: /todo
Request: 
```
mutation {
  update_todo_list: updateTodoList(task: "Hello Trial Final Updated", id: 17, createdBy:1, isComplete:false) {
    toDoList {
      task
      createdBy
      isComplete
    }
  }
}
```
Response:
```
{
  "data": {
    "update_todo_list": {
      "toDoList": {
        "task": "Hello Trial Final Updated",
        "createdBy": 1,
        "isComplete": false
      }
    }
  }
}
```
###### Delete TODO Task API
Path: /todo
Request: 
```
mutation {
  delete_todo_list: deleteTodoList( id: 17) {
    toDoList {
      task
      createdBy
      isComplete
    }
  }
}
```
Response:
```
{
  "data": {
    "delete_todo_list": {
      "toDoList": {
        "task": "Hello Trial Final Updated",
        "createdBy": 1,
        "isComplete": false
      }
    }
  }
}
```

## License
MIT
**Free Software, Hell Yeah!**


  
