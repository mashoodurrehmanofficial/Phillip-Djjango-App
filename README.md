# Phillip-Djjango-App


1. **Step 1**
    * Connect django to a Postgres Server and change the credential in PROJECT > settings.py inside variable DATABASES = {}

    * Then make database migrations by running follwoing commands
    * python manage.py makemigrations
    * python manage.py migrate

2. **Step 2**
    *  Create a  superuser by running followinf command and remember the credentials that you will steup
    * python manage.py createsuperuser
    * Link to Django Admin http://localhost:8000/admin
    * Now go to the highlighted tables on left side and creeate the required entries as shown in respective screenshots

    * ![SS1](https://raw.githubusercontent.com/mashoodurrehmanofficial/Phillip-Djjango-App/main/Static/images/ss1.PNG)
    - - -
    # GOOGLE Creds
    * Client ID     = 879545715675-dnu6nf0mbu8pus5ktjol8s2ou9pp1l3j.apps.googleusercontent.com
    * Secret_Key    = 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

    * ![SS2](https://raw.githubusercontent.com/mashoodurrehmanofficial/Phillip-Djjango-App/main/Static/images/ss2.PNG)

 



    * In case you are unable to configure the settings and database then you can have a look at the default sqlite3 dataabse by commenting and un-commenting few lines in settings.py
    * ![SS3](https://raw.githubusercontent.com/mashoodurrehmanofficial/Phillip-Djjango-App/main/Static/images/ss3.PNG)
