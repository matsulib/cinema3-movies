#!/bin/sh

cd `dirname "${0}"`/../..

mongod > out.log 2> err.log & 

pip3 install -r requirements.txt

python3 database/manage.py
PYTHONPATH=. pytest -v --cov=services
