Starting guide
==============

Working with local server
-------------------------

When all installations are done, you can now launch the application locally:

.. code-block:: console

   (.venv) $ python manage.py runserver

When the command is executed, you will see this in your terminal:

.. code-block:: console
   
   $ python manage.py runserver
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).
   January 05, 2024 - 11:50:31
   Django version 5.0, using settings 'oc_lettings_site.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.


You can use your web browser and check the
website that was started locally on your computer **http://localhost:8000/**

You can also make all modifications that Django allows, such as database migrations,
customizing templates, adding new functions...

.. note::

   It is recommended to create a new Git branch before doing anything with the code.

Testing and linting
-------------------

If you modified / add something, you can test the app locally by using:

.. code-block:: console

   (.venv) $ pytest

For deploying, all tests have to be okay, and the test coverage must be greater than 80%.

Then you can use a linting tool to check if the code is in compliance with PEP8:

.. code-block:: console

   (.venv) $ flake8

Deploying 
---------

To deploy your modifications, you need to commit your changes to the master branch of this application.
It will automatically launch the CI/CD pipeline.
If everything is fine, you will see your updates in a few minutes on the `website url <https://kolobov-p13-10017e0c2e8f.herokuapp.com/>`_.

If something is wrong, you have to check the logs on the CircleCI project's `repository url <https://app.circleci.com/pipelines/circleci/MB19RQ11fKgKiPrdTpWVhS/EkPbzaTzYVd4QEaKADfGnV>`_.
