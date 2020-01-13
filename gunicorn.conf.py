import multiprocessing
from globals import IP, PORT

bind = f'{IP}:{PORT}'  # address and port
# workers = multiprocessing.cpu_count() * 2 + 1   # nbr of workers
workers = 3
threads = 1     # number of threads per worker
timeout = 30  # seconds
max_requests = 500  # number of requests per worker before restarting the worker
keepalive = 5  # seconds to wait for requests on a Keep Alive connection with dir. connection to the client
# (remove above if you have a load balancer)
# capture_output = True     # write stdout to errorlog, no log active, hence disabled
