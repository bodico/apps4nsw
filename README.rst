Some project
============

Installation
------------

(assumes you have python, virtualenv and pip installed already)::

  mkdir apps4nsw
  virtualenv apps4nsw
  cd apps4nsw
  git clone git@github.com:bodico/apps4nsw.git
  cd apps4nsw
  pip install -r requirements.txt


Start dev server
----------------

To run a development server on your local instance::

  cd project/
  ./manage.py runserver

You should then see the site running at http://127.0.0.1:8000



