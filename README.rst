sendriot
========

sendriot is a smal python script to send messages (nagios) from console to matrix.riot server, uses matrix_client lib

install matrix_client
=====================
.. code:: bash
	install: apt-get install python-setuptools (if needed)
	download: https://github.com/matrix-org/matrix-python-sdk
	unzip and do
	python setup.py build
	python setup.py install

Use
===

auth data:
.. code:: json
	{
	     "username":"@blub:matrix.blub.de",
	     "password":"xxxx",
	     "server":"https://matrix.blub.de:443",
	     "roomid":"!blublub:matrix.blub.de",
	     "token":"adlfjaodfjfaodfjadosfundsoweiter"
	}
