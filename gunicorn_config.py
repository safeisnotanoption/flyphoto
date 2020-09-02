# Number of workers = num_of_cores * 2 + 1

command = '/home/sinao/flyphoto/env/bin/gunicorn'
pythonpath = '/home/sinao/flyphoto'
bind = '127.0.0.1:8001'
workers = 3
user = 'sinao'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=flyphoto.settings'
