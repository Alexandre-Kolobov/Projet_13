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

Installation of dependencies
----------------------------

Before use the app you have to install all python dependencies:
.. code-block:: console

   (.venv) $ pip install -r requirements.txt