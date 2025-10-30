@echo off

:: Install dependencies
pip install -r requirements.txt

:: Collect static files
python manage.py collectstatic --no-input

:: Apply any outstanding migrations
python manage.py migrate