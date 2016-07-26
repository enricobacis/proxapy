Proxapy
=======

Simple API proxy that uses Flask/requests/gunicorn.

Use cases
---------

-  **Centralize API requests** - Sometimes only a specific IP can access
   APIs. Run Proxapy on that machine and access the API from everywhere.

-  **Implement custom pre/post operation on API request/response** -
   Fork the project, add routes and implement your changes. Common
   changes include content filtering, add authentication key header not
   known by the end user.

Usage
-----

1. Make sure you have `virtualenv`_
2. ``make run``
3. Visit ``http://<proxyhost>:<proxyport>/<API>`` to access
   ``http://<API>``

By default ``<proxyhost>`` is bound to ``0.0.0.0`` and ``<proxyport>``
to ``5000``, so for example you could run Proxapy and then visit:
http://localhost:5000/api.left-pad.io/?str=proxied&len=20

.. _virtualenv: https://virtualenv.pypa.io
