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
Third, you need to import locations. You can do it manually using admin panel or load them using command:
```
python manage.py load_place LINK_TO_JSON
```
Json example: https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%AF%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%B0%D0%B4.json

## Environment variables

The code needs .env file with such environment variables as:

```
SECRET_KEY = you need one to run the project, keep it in secret!
DEBUG = should be True if you are in development mode and should be False if in production
```
## Running

The code should be ran in cmd like so:

```
python manage.py runserver
```