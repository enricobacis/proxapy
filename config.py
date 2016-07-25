# gunicorn config that can be used as:
#   gunicorn -c config.py proxy:app

bind = '0.0.0.0:5000'
workers = 4
errorlog = '-'
loglevel = 'info'
accesslog = '-'
