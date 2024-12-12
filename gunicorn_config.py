import multiprocessing

# Server socket
bind = "0.0.0.0:9000"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2

# Logging
accesslog = "../logs/gunicorn-access.log"
errorlog = "../logs/gunicorn-error.log"
loglevel = "info"

# Timeout
timeout = 30
