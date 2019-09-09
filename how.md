1. Instance who firstly creates a service endpoint is the leader of this service at very beginning. This instance then adds (control plane.alpha.kubernetes.io/leader) annotation to expose leadership information to other followers or application in the cluster.

2. The leader instance shall constantly renew its lease time to indicate its existence. In below, the leaseDuration is 15 seconds. The leader will update lease time (renewTime) before lease duration is expired.

3. Followers will constantly check the existence of service endpoint and if it is created already by the leader then the followers will do an additional lease (renewTime) renew checking against the current time. If lease time (renewTime) is older than Now which means leader failed to update its lease duration, hence suggests Leader is crashed or something bad has happened. In that case, a new leader election process is started until a follower successfully claims leadership by updating endpoint with its own Identity and lease duration.

How to create an endpoint:  
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#create_namespaced_endpoints

How to read an endpoint:  
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#read_namespaced_endpoints

How to update an endpoint:  
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#patch_namespaced_endpoints  
OR  
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#replace_namespaced_endpoints
