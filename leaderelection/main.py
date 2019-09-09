import logging.config
from os import path
from kubernetes import client
from pythonjsonlogger import jsonlogger
from .k8s import k8s_info, create_endpoint, list_endpoints


class Elect:
    def __init__(self):
        pass

    def poll(self):
        pass

    def run(self):
        # Logging config
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
        logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
        logger = logging.getLogger(__name__)

        # Create a CoreV1Api instance
        configuration = client.Configuration()
        CoreV1Api = client.CoreV1Api(client.ApiClient(configuration))

        # Return dictionary with controller information
        controller_dict = k8s_info()

        # If endpoint does not exist, create it and assume leadership.
        if not check_endpoint(CoreV1Api, controller_dict['namespace'], controller_dict['deploymentName']):
            create_endpoint(CoreV1Api, controller_dict['namespace'], controller_dict['body'])
        # Else start to poll for leadership status
        else:
            poll(CoreV1Api, controller_dict)
