# DjangoGamersAPI
Shows Auth concepts for multi-users and Django Rest Framework implementation of JWT

## Clone Project

    $ git clone git@github.com:fatahrez/DjangoGamersAPI.git
    $ cd DjangoGamersAPI

### Add .env file
    
    $ cp env.sample .env

Edit environment variables after copying from file env.sample. make sure to change your DATABASE_URL to match the db you created

#### Build project:
    
    $ pipenv shell
    
    $ pipenv sync
    
Read more about Pipenv installation and usage [using this link](https://github.com/pypa/pipenv)

#### Migrate database:

    $ python manage.py makemigrations
    
    $ python manage.py migrate

start with makemagrations before migrating your database


