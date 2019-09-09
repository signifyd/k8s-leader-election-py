import logging.config
import time
from os import sys, path
from kubernetes import config
from pythonjsonlogger import jsonlogger

if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from leaderelection import Elect

# Logging config
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# K8s authentication
try:
    config.load_incluster_config()
except:
    logger.info("Can't use incluster config. Attempting to use ~/.kube/config")
    config.load_kube_config()

if __name__ == '__main__':
    leaderelection = Elect()
    leaderelection.run()
    while True:
        logger.info("I am the leader.")
        time.sleep(6)
