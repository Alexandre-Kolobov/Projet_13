Installation
============

Creation of virtual environment
-------------------------------

To create virtual environment, move to the directory you want and do this command in your terminal:

.. code-block:: console

   $ python -m venv venv


Activation and deactivation of virtual environment
--------------------------------------------------
To activate virtual environment, use this command in your terminal:

.. code-block:: console

   $ source venv/Scripts/activate

To deactivate vitual envrionment, use this command in your terminal:

.. code-block:: console

   (.venv) $ diactivate


Clone code source repository
----------------------------

To pull code on your computer you can use:

.. code-block:: console

   (.venv) $ git clone git@github.com:Alexandre-Kolobov/Projet_13.git

.. note::

   You have to create an account on  `GitHub <https://github.com/>`_


.. _requirements:

Installation of dependencies
----------------------------

Before use the app you have to install all python dependencies:
.. code-block:: console

   (.venv) $ pip install -r requirements.txt

Here the content of requirements file:
   .. literalinclude:: ../../requirements.txt
      :language: text



Sentry  
-------

It is an application monitoring and debugging platform.
To set up it for our website you have to:

   - Create a sentry account.
   - Create a new DJANGO project.
   - Retrieve and save the given Sentry DNS key


Set up environment varibales
----------------------------
You have to set up 2 environment varibales: DJANGO_SECRET_KEY and SENTRY_KEY

   - **SENTRY_KEY** corresponding to Sentry DNS key that you get
   - **DJANGO_SECRET_KEY** is a confidential key in Django for securing passwords, cookies, and preventing CSRF attacks.

   .. note::

      You have to set up it twice: for working localy and on Heroku