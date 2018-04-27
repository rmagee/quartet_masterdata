=====
Usage
=====

To use quartet_masterdata in a project, add it to your `INSTALLED_APPS`:

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
