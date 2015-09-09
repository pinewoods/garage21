pyvenv env
source env/bin/activate
pip install -r requirements.txt
git clone https://github.com/django-notifications/django-notifications.git
cd django-notifications/
python setup.py install
cd ..
pytohn manage.py migrate
python manage.py runscript `populate_db`
cp `dashboard/local_settings.py.prod` `dashboard/local_settings.py`
