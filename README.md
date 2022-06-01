## Project Title

### Anime | Gallery

##Project Description

This is a photo gallery Django web application. A user can veiw photos according to category and location of the image.


### User story
- User can veiw different photos 
- User can veiw image modal with image description, location an category
- Copy image link


## Installing

- Copy this ![link]https://github.com/SarahK95/photogallery.git repository 
- Clone the repo to your terminal
- Run the code on a virtual enviroment and also have django installed
- For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
- To run the app, you'll have to run the following commands in your terminal

       pip install -r requirements.txt
1. On your terminal,Create database gallery using the command below.


       CREATE DATABASE imagegallery;
2. Migrate the database using the command below


       python3.6 manage.py migrate
3. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
4. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Prerequisites

- Python3
- Django
- virtual environment


## Deployment
- log in to heroku
```
heroku login
```
- create heroku app
```
heroku create app
```
- Upload requirements
```
pip freeze
```
- create a postgres addon to your heroku app
```
heroku addons:create heroku-postgresql:hobby-dev
```
- push to heroku

```
git push heroku master
```
- run migrations
```
heroku run python manage.py migrate
```

## Licence
- MIT License
- Copyright (c) 2022 Sarah Kamunya
