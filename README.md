#How setup

##Create virtual ENV

- python3 -m venv env

##Cli install Django

- pip install django

* django-admin
* django-admin startproject <project name> .

#How start project

- python manage.py runserver

#How to create app inside Django

- python manage.py startapp <app name>

#How django general static root folder

- python manage.py collectstatic

define static file to root folder

# Django connect with postgresql

\* Need to install driver

`pip instal psycopg2

pip install psycopg2-binary`

# For Check what migrations do

`python manage.py sqlmigrate <migrations file name>` `number`
`python manage.py sqlmigrate listings 0001`

# Make migrations?

`python manage.py makemigrations`
this cli it for create migration file from "Model" every app
if you want only one or new model, you can put model name as param like
`python manage.py makemigrations contacts`

then use
`python manage.py migrate`
this cli it'll take all migration file to database

# User, Password

user: codewizz
pass: 123456

user: evadaisie
pass: eve555%%

# Contact section

`python manage.py startapp contacts`
