## CSCI e33a Fall 25 Section2 Piano inventory Demo app
#### Django application using a Django session object for data persistence.
This app can create, edit and delete pianos. This is similar to what is being asked for in the current assignment where encyclopedia entries are created, edited and stored.  In this app a piano can be created by one of two methods: 1) an HTML form or 2) a Django form.

Session storage is a connection between a particular user's browser and the Django server.  The session object in this app is structured as a list of dictionaries which is similar to the structure of Django model objects (database) which will be addressed in the next lecture.
