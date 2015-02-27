****************************************
cloudmesh_database
****************************************

Database connection management for cloudmesh projects.

How to install
----------------------------------------------------------------------

First git clone the code from this repo. Before the installation we recommend to activate a virtualenv envrionment.

Install reqruiements

* pip install -r requirements

Install cloudmesh_database package

* python setup.py install

Copy configuration file to location

* python setup.py yaml


Example to use
----------------------------------------------------------------------

* cd examples

* python example1.py

In example1.py file this is a simple example about how to define mongonengine object and interact with db.


DB steup and configuratons
----------------------------------------------------------------------

* DB setup initiation has to be done externaly by related cloudmesh_admin commands or fab commands (fab monogo.reset)

* To add a new db/collection, modify the cloudmesh_database.yaml fiel. In the 'collections' section, add the collection name as key ('example') and the db name under it as the value ('db: exampledb'). After this the db has to be reset (currently fab mongo.reset).
