zayalabs
========

trello like app

Basic Commands
--------------
create virtualenv
python3.6 -m venv  venv
source venv/bin/activate
create database postgres *zayadb*
export env variable

export DATABASE_URL=postgres://username:userpassword@127.0.0.1:5432/zayadb

python manage.py makemigrations
python manage.py migrate



Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.



REST API Endpoints
^^^^^^^^^^^^^^^^^^^^^
login through ui 
check 127.0.0.1:8000/rest-docs
find api and check them through drf version ui (for better operation)

main 

http://127.0.0.1:8000/api/



http://127.0.0.1:8000/api/tasks/board/   (GET POST PUT DELETE)
http://127.0.0.1:8000/api/tasks/list/    (GET POST PUT DELETE)
http://127.0.0.1:8000/api/tasks/card/    (GET POST PUT DELETE)