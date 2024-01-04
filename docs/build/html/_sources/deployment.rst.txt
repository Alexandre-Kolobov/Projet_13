Deployment
==========
Deployment is set up using a CI/CD pipeline,whe commit on the master branch.

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