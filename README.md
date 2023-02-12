# Sightseeings map by Artem

Map of Moscow by Artem to show his favourite sightseeings, museums etc.
Check it out: http://eshinanase.pythonanywhere.com/

## Prerequisites

Virtual environment needs to be:

```
python==3.9
```
## Installing

First, you need to clone the code:

```
git clone https://github.com/EshiNanase/afisha.git
git checkout pro
```
Second, you need to install requirements.txt:

```
pip install -r requirements.txt
```
## Environment variables

The code needs .env file with such environment variables as:

```
SECRET_KEY = django project secret key
DEBUG = true/false
```
## Running

The code should be ran in cmd like so:

```
python manage.py runserver
```