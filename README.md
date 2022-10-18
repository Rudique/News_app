## News_app
Django app, you can add posts and comment them

## How to start

1) Clone app from repository with command in terminal:
    <p>git clone https://github.com/Rudique/News_app.git</p>

2) Install dependencies from requirements.txt with command:
    <p>pip install -r requirements.txt</p>

3) Create superuser to manage the admin panel:
   <p>python3 manage.py createsuperuser</p>
4) Make migrations with 2 commands:
   <p>python3 manage.py makemigrations</p>
   <p>python3 manage.py migrate</p>
5) Run app with command:
   <p>python3 manage.py runserver</p>

## Urls
1) /admin - admin panel, where you can add users, news, comments and edit them
2) /news - listview of all news
3) news/new - adding new post 