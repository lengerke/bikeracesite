# Bike Race Site
This repo is a work in progress website based on Django. Its purpose is to help organize a multi-stage bike race with many cyclists grouped up into several teams.

# Installation
## Importing the project
In a suitable folder do the following
```
git clone https://github.com/lengerke/bikeracesite.git
```
## Dependencies
- Python 3.8
- Django 4.2.17
After innstalling Python, you may want to configure a separate ```venv``` environment in the project folder, e.g., via
```
cd bikeracesite/
python -m bikeracevenv .venv
source .venv/bin/activate
```
To install Django follow this [guide](https://docs.djangoproject.com/en/5.1/intro/install/) that can be boiled down to
```
python -m pip install Django
```
You also need bootstrap
```
python -m pip install django-bootstrap-v5
```
