import time
import logging
from kubernetes import config
from threading import Thread
from leaderelection import Elect

# K8s authentication
try:
    config.load_incluster_config()
except:
    config.load_kube_config()

if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Init leader election class
    leaderelection = Elect(configmap='sample-controller-leader-election')
    # Run leader election in new thread
    th = Thread(target=leaderelection.run)
    th.setDaemon(True)
    th.start()
    while True:
        # Check if im the leader. If so continue on with controller logic.
        leader = leaderelection.check_leader()
        if leader:
            logger.info("I am the leader!!")
        else:
            logger.info("I am NOT the leader")
        time.sleep(5)
