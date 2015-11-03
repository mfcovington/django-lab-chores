*****************
django-lab-chores
*****************

``django-lab-chores`` is a Django app for assigning and tracking lab chores for scientists in a lab. It uses ``django-lab-members`` to populate the list of lab members that will be assigned chores.

Source code is available on GitHub at `mfcovington/django-lab-chores <https://github.com/mfcovington/django-lab-chores>`_. Information about and source code for ``django-lab-members`` is available on GitHub at `mfcovington/django-lab-members <https://github.com/mfcovington/django-lab-members>`_.

.. contents:: :local:


.. Installation
.. ============

.. **PyPI**

.. .. code-block:: sh

..     pip install django-lab-chores

.. **GitHub**

.. .. code-block:: sh

..     pip install https://github.com/mfcovington/django-lab-chores/releases/download/0.0.0/django-lab-chores-0.0.0.tar.gz


Configuration
=============

Do the following in ``settings.py``:

- Add ``lab_chores`` and its dependencies to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'easy_thumbnails',
        'filer',
        'friendlytagloader',
        'lab_chores',
        'lab_members',
        'mptt',
        'sekizai',
    )


- Specify your media settings, if necessary:

.. code-block:: python

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


- Add ``filer`` and ``easy_thumbnail`` settings: 

.. code-block:: python

    # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
    THUMBNAIL_HIGH_RESOLUTION = True
    THUMBNAIL_QUALITY = 95
    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )
    THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
    THUMBNAIL_SUBDIR = 'versions'


Migrations
==========

Create and perform ``lab_chores`` migrations:

.. code-block:: sh

    python manage.py makemigrations lab_chores
    python manage.py migrate


Usage
=====

- Start the development server:

.. code-block:: sh

    python manage.py runserver


- Login to add/assign lab chores: ``http://localhost:8000/admin/lab_chores/``
- View lab chore assignments: ``http://127.0.0.1:8000/lab_chores/``


*Version 0.0.0*
