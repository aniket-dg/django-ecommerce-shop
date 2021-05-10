# django-ecommerce-shop
Ecommerce Webs App using Django Python Framework
## Installation
```
git clone https://github.com/aniket-dg/django-ecommerce-shop.git
```
Create a VirtualEnv for Python3 and Activate it

Go to the Project Folder
```
cd django-ecommerce-shop
```
Install all required Libraries
```
pip install -r requirements.txt
```
## Database Configuration
  1. Create database 'shop' using pgAdmin.

## Environment File
1. Create .env file in root folder (i.e. inside django-ecommerce-shop/) using vscode terminal or using git bash.
1. Open .env file, Create following 3 variables. 
     <br> SECRET_KEY = 'create new secret key using online tool'<br>
      USER = 'your database user name'<br>
      PASSWORD = 'your database password'<br>
 2. Save file.
 
 Apply Migrations
```
python manage.py migrate
```
 Create Super User
 Remember your username and password.
```
python manage.py createsuperuser
```
Start the Project
```
python manage.py runserver
```
Go to the [localhost](http://127.0.0.1:8000/)

Add Some data for working properly
  1. Go to [adminPanel](http:127.0.0.1:8000/admin)
  2. Enter your credentials you created in the previous step
  3. Add some shoes.
  
## Your app is ready :)
