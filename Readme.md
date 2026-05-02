# Project lab Backstage:

```bash
docker build -t python-app:1.0 .
docker run --rm -p 8080:5000  python-app:1.0
```
```sh
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
```
```sh
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace
```
```sh
helm create python-app      ## Cria a estrutura base de pastas e arquivos
cd charts\python-app
helm install python-teste -n python . --create-namespace
```
```sh
http://github.com/argoproj/argo-helm/tree/main/charts/argo-cd

helm repo add argo https://argoproj.github.io/argo-helm .
helm repo update
helm upgrade --install argocd argo/argo-cd --namespace argocd --create-namespace -f values-argo.yaml

admin
iJeRyswywFWMIuwL
VK568kpjXWZpCD0g
```