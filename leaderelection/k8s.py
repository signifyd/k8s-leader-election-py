import logging.config
import os
from kubernetes import client
from kubernetes.client.rest import ApiException
from pythonjsonlogger import jsonlogger

# Logging config
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def k8s_info():
    deploymentName = 'test'
    namespace = 'default'
    #namespace = open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
    body = client.V1Endpoints(
        metadata.name = deploymentName,
        metadata.name = namespace,
        metadata.annotations = 'control.plane.alpha.kubernetes.io/leader'
    )

    controller_dict = {
        'deploymentName' = deploymentName
        'namespace': namespace,
        'body': body
    }
    return controller_dict

def check_endpoint(CoreV1Api, namespace, deploymentName):
    endpoints = CoreV1Api.list_namespaced_endpoints(namespace)
    for endpoint in endpoints.items:
        if endpoint.metadata['name'] == deploymentName:
            return True
    return False


def create_endpoint(CoreV1Api, namespace, body):
    try:
        response = CoreV1Api.create_namespaced_endpoints(namespace, body)
        logger.info(response)
    except ApiException as e:
        logger.error("Exception when trying to create the endpoint: %s\n" % e)
