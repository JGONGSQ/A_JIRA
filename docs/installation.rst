# Installations:

    ## Requirements:
    - Python 3
    - Pip3
    - mysql
    - virtualenv

    ## Steps:
        1. Set up venv.
            - In PyCharm do (File->Settings->Project: foo->Project Interpreter->click cog icon->create new VirtualEnv)
        2. Install Pillow requirements `libfreetype`, `libjpeg` and `zliblg-dev`.
            See http://pillow.readthedocs.org/en/3.0.x/installation.html

        3.Install Python requirements.
        - In PyCharm open requirements.txt to get PyCharm to prompt you

        4. Run`python manage.py. makemigration` than Run `python manage.py migrate`.
        - Multiple times if it fails the first time.

        5. run `initial_database_setup`

    ## Running

    `python3 manage.py runserver`
    - Try to log in with the admin user that you created earlier.