# BrewPi web service
[![Code Climate](https://codeclimate.com/github/BrewPi/brewpi_webservice/badges/gpa.svg)](https://codeclimate.com/github/BrewPi/brewpi_webservice)

This is the very start of a new web service for BrewPi. It will provide a REST API to the BrewPi backend.
For our current production version, see [brewpi-www](https://github.com/BrewPi/brewpi-www)

# Install

Install [Python 3.5](https://www.python.org/downloads/)

Create a new virtualenv for brewpi_webservice. Easiest way to do this is with virtualenvwrapper. Install it through pip.

For Windows:

    pip install virtualenvwrapper-win
    
For other systems:
    
    pip3 install virtualenvwrapper
    

Create a new virtualenv:

    virtualenv -p python3 brewpiws
    

Now start using the virtualenv:
    
    source brewpiws/bin/activate


Install all required dependencies:

    pip install -r requirements.txt
    
# Setup

Initialize the database:

    python manage.py migrate
    
Create a superuser

    python manage.py createsuperuser
    
# Run

You can run the development server with:

    python manage.py runserver_plus

You can now point your browser to `http://localhost:8000` to access the
root API frontend or to `http://localhost:8000/admin/` for the
administration panel.



