- pyvenv env
- source env/bin/activate
- pip install -r requirements.txt
- git clone https://github.com/django-notifications/django-notifications.git
- cd django-notifications/
- python setup.py install
- cd ..
- pytohn manage.py migrate auth
- pytohn manage.py migrate
- python manage.py runscript `populate_db`
- cp `dashboard/local_settings.py.prod` `dashboard/local_settings.py`


# Configurando e fazendo Deploy
- Entra na pasta do repositorio
- git remote add live dokku@cineme.com.br:dashboard
- git add .
- git commit -m "comentario"
- git push live master
- Para publicar no bitbucket: git push origin master
- Para publicar no live: git push live master
