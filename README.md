# MicroK8s Cluster

### Structure

├── linky/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
|   └── kustomization.yaml
├── postgres/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
|   └── kustomization.yaml
└── kustomization.yaml   # kustomization


Deploy with:
```
kubectl apply -k .
```


### Add secrets
```
kubectl create secret generic linky-secrets \
  --from-literal=VUE_APP_SUPABASE_URL=secret1 \
  --from-literal=VUE_APP_API_KEY=secret2
```

### Layers
HTTP (your Vue app)
   ↑
TCP (transport protocol)
   ↑
IP  (network layer)

### Links
- How to deploy Vuejs App with Kubernetes: https://blog.openreplay.com/deploying-vue-apps-to-the-cloud-with-kubernetes/

### Internal Access Linky
- Access Linky: node-ip:NodePort-port - http://192.168.178.44:30080/

### External Access Linky
Loadbalancer not needed because 
- http://100.64.110.250:30080/#/

### NodePort vs Metallb LoadBalancer on FritzBox
https://microk8s.io/docs/addon-metallb
- NodePort exposes the service on the real node IP (192.168.178.44) on a high port (30080).
- FritzBox and all LAN devices can reach real physical IPs, so port forwarding works without any special configuration.
- LoadBalancer/MetalLB = virtual IP inside cluster → may not be reachable on home networks with consumer routers.
- NodePort = real node IP → works perfectly for LAN and internet via port forwarding