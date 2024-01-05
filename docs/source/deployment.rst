Deployment
==========

Description
-----------
Deployment is set up using a CI/CD pipeline, when commit on the master branch.

The deployment process consists of three steps:

    1) Unit testing and code linting
    2) If the previous step is successful, a Docker image is created and pushed to DockerHub
    3) If the previous step is successful, the code is deployed to Heroku

The CI/CD tools involved are:

    * Docker and DockerHub: Used to create and store images of our application
    * CircleCI: Sets up the pipeline for executing the CI/CD steps
    * Heroku: Hosts our application and makes it publicly accessible

The required configuration for successful deployment includes:

    * Unit tests and code linting should not report any errors
    * Code coverage must be greater than 80%
    * The Docker image must be created and pushed correctly to DockerHub with commit hash tag
    * Environment variables must be defined on Heroku


Pull docker Image
-----------------

Docker is a platform for launching applications using containers.
You have to install docker on you machine and create to a DockerHub account.

Docker : `Téléchargement de Docker <https://www.docker.com/get-started>`_.


In DockerHub, select the lastest image Tags of Repository : `Project repository <https://hub.docker.com/repository/docker/kolobov/p13_django_image/general>`_ .
 
Now you can pull the latest image on your machine:

.. code-block:: console

   (.venv) $ docker pull kolobov/p13_django_image:chosen_tag

Check any local server  is running and Run docker like that:

.. code-block:: console

   (.venv) $ docker compose up

In your browser, enter **localhost:8000** or click on link inside a console.
That will open the website locally.

To stop Docker:

.. code-block:: console

   (.venv) $ docker compose down


CircleCi configutation
----------------------
In CircleCi projet's settings, you have to define environment variable for:

.. code-block:: console

    DOCKER_USER = Your docker login
    DOCKER_PASSWORD = Your docker password
    HEROKU_TOKEN = Token from Heroku to allows CircleCI to push on Heroku


Heroku configutation
----------------------
In Heroku projet's settings, you have to define environment variable for:

.. code-block:: console

    DEBUG = To activate debug if you need (True or false)
    DJANGO_SECRET_KEY = Your django secret key
    HEROKU_TOKEN = Token from Heroku to allows CircleCI to push on Heroku
    SENTRY_KEY = Your key from Sentry to allow Heroku to push logs to Sentry

