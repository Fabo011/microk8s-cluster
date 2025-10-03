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

### Access Linky
- Access Linky: node-ip:NodePort-port - http://192.168.178.44:30080/