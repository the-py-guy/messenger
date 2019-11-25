# messenger
This project is aimed at creating an easy way to send and await email notifications in python projects. It was originally created to be used in junction with my ai_framework for communication with the ai via sms/email for a personal project of mine but I thought it was a useful module in general so I created this repository for it.

# Requirements
* smtplib
* time
* imaplib
* email
* __IMPORTANT: Make sure you allow "less secure apps" in gmail settings!__ https://support.google.com/a/answer/6260879?hl=en

# Installation / Basic Usage
1. Download messenger.py
2. Move messenger.py to your projects folder
3. Open messenger.py in a text editor of your choosing
4. Change line 3 to your gmail address
5. Change line 4 to your gmail password
6. Import messenger into your script

Once you have messenger imported, you can use __messenger.send(recipient, message)__ to send an email and to handle a response, you use __messenger.await_response()__ to wait until a response has been recieved. Apon recieving a response, "await_response()" will return the following response dictionary: {'sender':sender,'message':msg,'date':date,'time':time}.
