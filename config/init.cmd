cd C:\WebApps\games\games\__pycache__
del *.pyc
cd C:\WebApps\games\laby\migrations\__pycache__
del *.pyc
cd C:\WebApps\games\laby\migrations
del *.py
type NUL > __init__.py
cd C:\WebApps\games\laby\__pycache__
del *.pyc
cd C:\WebApps\games
del *.sqlite3

python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver