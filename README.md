# Interapp

Interview preparation web application.

These are more or less the steps to get it going:
````
1. Create virtual environment.
2. Clone the application.
3. Install requirements.
4. Create .env.
5. Create database.
6. Create superuser.
7. Enjoy!
````


## 1. Virtual Environment

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install a virtual environment.


Upgrade pip:
````shell
sudo pip install --upgrade pip
````


I personally use [virtual environment wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). However, I had to do a little extra work to make it work with python 3.9. 

Any python 3+ should work fine with this app.



Create venv:
```shell
mkvirtualenv -p python3.9 ENVNAME
```

Then make sure you see your environment in your terminal:

````shell
(ENVNAME) thiagoreis:~/Projects/interapp$ 
````

## 3. Install Requirements

````shell
pip install -r requirements.txt
````

## 4. Create .env:

````shell
touch .env
````
Copy and paste this inside of the .env file:

```
# SECURITY WARNING: don't run with the debug turned on in production!
DEBUG=True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY="REPLACE_THIS_STRING"

# PostgresSQL Database
DB_NAME="REPLACE_THIS_STRING"
DB_USERNAME="REPLACE_THIS_STRING"
DB_PASSWORD="REPLACE_THIS_STRING"
```

## 5. Create Database

PostgresSQL will be used as this project's database. 
A simple and good guide can be found [here](https://www.geeksforgeeks.org/how-to-use-postgresql-database-in-django/).

I also used PgAdmin to create a database. You don't have to but here is a [guide](https://stackoverflow.com/questions/8200917/postgresql-create-a-new-db-through-pgadmin-ui).

````shell
pip install psycopg2
````

````
Run your migrations.

```shell
python manage.py makemigrations
python manage.py migrate
````

## 6. Create a superuser

````shell
python manage.py createsuperuser
````


## 7. Enjoy

````shell
python manage.py runserver
````
Go to: http://127.0.0.1:8000/admin to add and edit questions.

ENJOY!


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)

