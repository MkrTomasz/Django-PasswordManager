# Django - Password Manager
current version: 1.0


Description:
------------------------
Password Manager is an application that serves as a wallet of passwords.   
User can store login credentials for web accounts and services to keep those in one place.


How to install and run:
------------------------
1. Download the project
2. Make sure to install requirements.txt
3. Go to the folder: django_pwdManager -> use command: *python manage.py runserver*
4. Open application in the browser and go to: http://127.0.0.1:8000/


How to use:
------------------------
Create your user account and log in. Click "Go to the list of passwords" and you will be redirected to the list of passwords added to your account.

### Password list:

Create new entry - user will be redirected to a form. To create a new entry fill out the form, which consists of the following fields:
1. Service name (required, 1-50 characters)
2. User name (required, 3-30 characters)
3. E-mail (optional)
4. Password (required, 3-30 characters)
5. Comment (optional)

Filter by service name field:
- Case insensitive
- User can provide only part of the service name to show a record
- Leave the field blank and hit SEARCH to remove all filters

You can modify and delete your entries at any time.

### Application account password reset:

You can change your password if you are logged in. If not, you can reset it by providing e-mail address used during the signup process, you will receive a link with further instructions (v 1.0 - link is generated in the Terminal)


Update log:
------------------------
### version 1.0:
1. Creation of user login system
2. Creation of a form that holds credentials for web account/service
3. Added ability to update and delete entries
4. Added password list filtering field
5. Creation of HTML templates
6. Integration of HTML templates with backend
