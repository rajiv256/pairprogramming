rm db.sqlite3
rm -rf user/migrations/__pycache__/
rm -rf user/migrations/00*
rm -rf project/migrations/__pycache__/
rm -rf project/migrations/00*
python manage.py makemigrations user
python manage.py makemigrations project
python manage.py migrate --run-syncdb

