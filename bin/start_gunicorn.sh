#!/bin/bash
source /home/sinao/flyphoto/env/bin/activate
exec gunicorn -c "/home/sinao/flyphoto/gunicorn_config.py" flyphoto.wsgi
