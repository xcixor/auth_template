Flask Authentication Template

Getting Started

    Prerequisites
    You should have the following software installed
        python 
        virtualenv
    Check online how to install those on your specific machine

    Installing
    To install the app, clone the project with the following command for mac and linux users
        $ git clone https://github.com/xcixor/auth_template
    Then, navigate to the project folder in terminal and create a virtual environment as follows,
        $ virtualenv myvenv
    After the virtual environment has been created activate it as follows,
        $ source myvenv/bin/activate
    Once the virtual environment is active, replicate the app's virtual environment by running the following command
        (myvenv) $ pip install -r requirements.txt
    Once installation is finished, set up the database by running the following commands
            (myvenv) $ python manage.py db init : creates a migrations folder, where all the migration scripts will be stored
            (myvenv) $ python manage.py db migrate -m "initial migration" : to create a migration script
            (myvenv) $ python hello.py db upgrade : creates the database
    Start the app by running;
            (myvenv) $ python manage.py runserver
    Navigate to the following link in your favorite browser
        http://localhost:5000/
    Enjoy!
    ps, for pc's come back later

Running the Tests

Deployment

Built with
    -Flask

Contributing

Versioning

Authors
	pndungu54@gmail.com
Licences

Acknowledments
