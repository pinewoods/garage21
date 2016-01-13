- pyvenv env
- source env/bin/activate
- pip install -r requirements.txt
- git clone https://github.com/django-notifications/django-notifications.git --branch 0.7.1
- cd django-notifications/
- python setup.py install
- cd ..
- python manage.py migrate auth
- python manage.py migrate
- python manage.py runscript `populate_db`
- cp `dashboard/local_settings.py.prod` `dashboard/local_settings.py`
- python manage.py createsuperuser



#troubleshoot for fucking PG
apt-get install libpq-dev python-dev
apt-get install libncurses5-dev
