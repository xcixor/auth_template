Flask Authentication Template

Getting Started

    Prerequisites
    You should have the following software installed
        python 3*
        virtualenv
    Check online how to install those on your specific machine

    Installing
    To install the app, clone the project with the following command for mac and linux users
        $ git clone https://github.com/xcixor/auth_template
    Then, navigate to the project folder in terminal and create a virtual environment as follows, assumming you are using python 3.5, else change it to mathch your version.
        $ python3.5 -m venv myvenv

    After the virtual environment has been created activate it as follows,
        $ source myvenv/bin/activate
    Once the virtual environment is active, replicate the app's virtual environment by running the following command
        (venv) $ pip install -r requirements.txt
    Once installation is finished, launch the app by running the following commands
        python manage.py shell - opens a python shell where you create the database as follows
            >>>db_create_all()
        after that, exit from the python shell and run;
            $ python manage.py runserver
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

Licences

Acknowledments
