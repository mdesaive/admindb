# About
Database with Django frontend to store various information for system administrators.

# Installation

## Create MySQL Database
In MySQL execute commands like to following. Take care to adapt database name, user name and password to your needs.

    create database admindb;
    grant all privileges on admindb.* to django@localhost identified by 'my_user_pass';
    quit

## Prepare VirtualEnv
### Compile Python 3.5

    sudo aptitude install sudo aptitude apt-file wget vim man zlib1g-dev libssl-dev openssl build-essential mysql-server libmysqlclient-dev python-virtualenv python3 python-pip python3-pip

    mkdir ~/src
    cd ~/src
    wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
    tar -xvJf Python-3.5.1.tar.xz
    cd Python-3.5.1
    ./configure --prefix ~/opt/  --with-ensurepip=install
    make && make altinstall

### Update PIP Packages

    sudo pip install -U pip
    sudo pip install -U virtualenv

### Create VirtualEnv

    virtualenv -p ~/opt/bin/python3.5 ~/dev/django-py35
    source ~/dev/django-py35/bin/activate
    pip install django django-bootstrap3 django-tables2 mysqlclient

## Clone admindb GIT Repository

    cd ~/dev/django-py35/projects/
    git clone https://github.com/mdesaive/admindb.git

## Configure admindb
    
    cp -p admindb/admindb/settings_secret.py.template admindb/admindb/settings_secret.py

Edit admindb/admindb/settings_secret.py

### Apply Migrations
    
    (source ~/dev/django-py35/bin/activate)
    cd ~/dev/django-py35/projects/admindb-medneo/admindb 
    python manage.py migrate

### Create Superuser
    
    python manage.py createsuperuser

## Start Django Testserver

    (source ~/dev/django-py35/bin/activate)
    cd ~/dev/django-py35/projects/admindb-medneo/admindb
    python manage.py runserver 0.0.0.0:8000

## Connect to Django Testserver

Connect to http://localhost:8000/admin/



