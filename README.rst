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
.. code-block:: bash

    {
        "username":"@blub:matrix.blub.de",
        "password":"xxxx",
        "server":"https://matrix.blub.de:443",
        "roomid":"!blublub:matrix.blub.de",
        "token":"adlfjaodfjfaodfjadosfundsoweiter"
    }

Use
===

.. code-block:: bash
  sendriot.py -a </path/to/matrix.json> [-d -p -e roomid]
           -d debug infos
           -p login with password, rahter token
           -e     : enter room  !blublbu:matrix.blub.de,
                    the roomid should be in .matrix.json file


You need a username+password+roomid+server, this must be set in matrix.json file.

Get the Token:
* echo "test"  | python sendrio.py -a /path/to/.matrix.json -d -p

Enter room with password:
* python sendrio.py -a /path/to/.matrix.json -d -p -e 

Enter room with token:
* python sendrio.py -a /path/to/.matrix.json -d -e

Send Messages:
echo "my Messages ...." | * python sendrio.py -a /path/to/.matrix.json


TODO
====

* store token in json
* try/exceptions 
