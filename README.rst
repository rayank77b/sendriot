sendriot
========

sendriot is a smal python script to send messages (nagios) from console to matrix.riot server, uses matrix_client lib

install matrix_client
=====================
.. code-block:: bash

   #install: 
   $ apt-get install python-setuptools (if needed)
   #download: 
   # https://github.com/matrix-org/matrix-python-sdk
   # unzip and do
   $ python setup.py build
   $ python setup.py install

Config
======

auth data:
.. code-block:: javascript

    {
      "username":"@blub:matrix.blub.de",
      "password":"xxxx",
      "server":"https://matrix.blub.de:443",
      "roomid":"!blublub:matrix.blub.de",
      "token":"adlfjaodfjfaodfjadosfundsoweiter"
    }

Use
===

At moment it login with token, therefore you need a token.

TODO
====

* debug info
* login from password or login from token
* store token in json
* try/exceptions 
