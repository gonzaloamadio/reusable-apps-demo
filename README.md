# Package

Create this repo to play with reusable apps.
There are 2 simple projects. One that creates a model in the db and another one that has DRF views to list users.

## TODO:

Finish this readme with all tests and conclusions

## Usage

## Build and install log

Build tutorial django app

```
❯ python setup.py sdist
running sdist
running egg_info
creating tutorial.egg-info
writing tutorial.egg-info/PKG-INFO
writing dependency_links to tutorial.egg-info/dependency_links.txt
writing requirements to tutorial.egg-info/requires.txt
writing top-level names to tutorial.egg-info/top_level.txt
writing manifest file 'tutorial.egg-info/SOURCES.txt'
reading manifest file 'tutorial.egg-info/SOURCES.txt'
writing manifest file 'tutorial.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

running check
creating tutorial-0.1.0
creating tutorial-0.1.0/quickstart
creating tutorial-0.1.0/quickstart/migrations
creating tutorial-0.1.0/tutorial
creating tutorial-0.1.0/tutorial.egg-info
copying files to tutorial-0.1.0...
copying setup.py -> tutorial-0.1.0
copying quickstart/__init__.py -> tutorial-0.1.0/quickstart
copying quickstart/admin.py -> tutorial-0.1.0/quickstart
copying quickstart/models.py -> tutorial-0.1.0/quickstart
copying quickstart/serializers.py -> tutorial-0.1.0/quickstart
copying quickstart/tests.py -> tutorial-0.1.0/quickstart
copying quickstart/views.py -> tutorial-0.1.0/quickstart
copying quickstart/migrations/__init__.py -> tutorial-0.1.0/quickstart/migrations
copying tutorial/__init__.py -> tutorial-0.1.0/tutorial
copying tutorial/settings.py -> tutorial-0.1.0/tutorial
copying tutorial/urls.py -> tutorial-0.1.0/tutorial
copying tutorial/wsgi.py -> tutorial-0.1.0/tutorial
copying tutorial.egg-info/PKG-INFO -> tutorial-0.1.0/tutorial.egg-info
copying tutorial.egg-info/SOURCES.txt -> tutorial-0.1.0/tutorial.egg-info
copying tutorial.egg-info/dependency_links.txt -> tutorial-0.1.0/tutorial.egg-info
copying tutorial.egg-info/not-zip-safe -> tutorial-0.1.0/tutorial.egg-info
copying tutorial.egg-info/requires.txt -> tutorial-0.1.0/tutorial.egg-info
copying tutorial.egg-info/top_level.txt -> tutorial-0.1.0/tutorial.egg-info
Writing tutorial-0.1.0/setup.cfg
creating dist
Creating tar archive
removing 'tutorial-0.1.0' (and everything under it)
```

Install it on a venv with python 3.7

```
❯ pip install tutorial-0.1.0.tar.gz
Looking in indexes: https://pypi.org/simple, https://pypi.apeeldata.com
Processing ./tutorial-0.1.0.tar.gz
Requirement already satisfied: django in /Users/gonzaloamadio/.virtualenvs/py37/lib/python3.7/site-packages (from tutorial==0.1.0) (3.2.3)
Requirement already satisfied: djangorestframework in /Users/gonzaloamadio/.virtualenvs/py37/lib/python3.7/site-packages (from tutorial==0.1.0) (3.12.4)
Requirement already satisfied: sqlparse>=0.2.2 in /Users/gonzaloamadio/.virtualenvs/py37/lib/python3.7/site-packages (from django->tutorial==0.1.0) (0.4.1)
Requirement already satisfied: pytz in /Users/gonzaloamadio/.virtualenvs/py37/lib/python3.7/site-packages (from django->tutorial==0.1.0) (2021.1)
Requirement already satisfied: asgiref<4,>=3.3.2 in /Users/gonzaloamadio/.virtualenvs/py37/lib/python3.7/site-packages (from django->tutorial==0.1.0) (3.3.4)
Requirement already satisfied: typing-extensions in /Users/gonzaloamadio/.virtualenvs/py37/lib/python3.7/site-packages (from asgiref<4,>=3.3.2->django->tutorial==0.1.0) (3.10.0.0)
Building wheels for collected packages: tutorial
  Building wheel for tutorial (setup.py) ... done
  Created wheel for tutorial: filename=tutorial-0.1.0-py3-none-any.whl size=5344 sha256=b94a9daa41d1551fc543b2798148c310c183d721517ac380eb1bfb347623ed70
  Stored in directory: /Users/gonzaloamadio/Library/Caches/pip/wheels/d9/54/1f/2e2803af3f55aa3d401a2670284cdc4812503a63b16fd54b94
Successfully built tutorial
Installing collected packages: tutorial
Successfully installed tutorial-0.1.0
```
