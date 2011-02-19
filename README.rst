Some project
============

Installation
------------

(assumes you have python, virtualenv and pip installed already)::

  mkdir apps4nsw
  virtualenv apps4nsw
  cd apps4nsw
  git clone git@github.com:bodico/apps4nsw.git
  source bin/activate
  cd apps4nsw
  pip install -r requirements.txt


Start dev server
----------------

To run a development server on your local instance::

  cd project/
  ./manage.py runserver

You should then see the site running at http://127.0.0.1:8000


pyCharm config
--------------

If you're using pyCharm (or some other fancy IDE) then you need to 
configure it to refer to the python binary in your virtualenv.

i.e. Preferences > Python Interpreter

* remove any interpreter pyCharm found by itself
* add /YOURWORKSPACE/apps4nsw/bin/python

then click 'Apply'

Go to 'Django Support' and 'Enable Django Support'.

* set Django project root as /YOURWORKSPACE/apps4nsw/apps4nsw/project

pyCharm should now find settings.py and manage.py.

Add /YOURWORKSPACE/apps4nsw/apps4nsw/templates as a templates directory.

then click 'Apply'


Create site database
--------------------

Create the db::

  cd project/
  ./manage.py syncdb
  ./manage.py migrate


Load in data
------------

If you want to get off the ground quickly, simply load the pets data
fixtures::

  ./manage.py loaddata pets/fixtures/pets.json

Or if you need to recreate the data from scratch, run these scripts in
sequence::

  ./manage.py geocode_postcodes
  ./manage.py load_dogs_by_suburb
  ./manage.py flatten_postcodes
  ./manage.py aggregate_totals

