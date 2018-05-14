=============================
quartet_masterdata
=============================

.. image:: https://gitlab.com/serial-lab/quartet_masterdata/badges/master/coverage.svg
   :target: https://gitlab.com/serial-lab/quartet_masterdata/pipelines
.. image:: https://gitlab.com/serial-lab/quartet_masterdata/badges/master/build.svg
   :target: https://gitlab.com/serial-lab/quartet_masterdata/commits/master
.. image:: https://badge.fury.io/py/quartet_masterdata.svg
    :target: https://badge.fury.io/py/quartet_masterdata

Models and APIs to support material, lot and location master data.

Documentation
-------------

The full documentation is at https://serial-lab.gitlab.io/quartet_masterdata/

OpenFDA API Key
---------------
You will need an OpenFDA API Key to import master material data on-demand.
In addition, in your `qu4rtet` `.env` file, you will need to enter the following
configuration value as below.

To get a free OpenFDA key go here:

    https://open.fda.gov/api/reference/

.. code-block:: text

    ### ONLY AN EXAMPLE ###
    OPEN_FDA_API_KEY=is:jKdYth4jNRTWTu9LzHmc1ftrpuVomkpsz6hdefiD #only an EXAMPLE

Quickstart
----------

Install quartet_masterdata::

    pip install quartet_masterdata

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'quartet_masterdata.apps.QuartetMasterdataConfig',
        ...
    )

Add quartet_masterdata's URL patterns:

.. code-block:: python

    from quartet_masterdata import urls as quartet_masterdata_urls


    urlpatterns = [
        ...
        url(r'^', include(quartet_masterdata_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
