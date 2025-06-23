# End-to-End CI/CD on GCP with Terraform, FastAPI, Docker & Kubernetes

This project demonstrates a complete DevOps pipeline — from infrastructure provisioning on **GCP** using **Terraform**, to containerizing **FastAPI microservices** with **Docker**, and deploying them to **GKE (Google Kubernetes Engine)** using **Kubernetes**.

---

## How to Use

### 1. Clone the Repository

### 2. Provision GCP Infrastructure
This step creates cloud resources — do it only after GCP setup.
cd infra
terraform init
terraform plan
terraform apply

This will:
Create a custom VPC and subnet
Provision a GKE cluster
Set up networking for deployment. You can create your own vpc or use a default vpc as well. 

### 3. Run Microservices Locally
To test users microservice:
cd services/users
pip install -r requirements.txt
uvicorn app:app --reload

for example:
![image](https://github.com/user-attachments/assets/213371ca-e7a7-4535-bcae-6ffb39fc21ba)

testing done locally:
![image](https://github.com/user-attachments/assets/6bc7bbe5-5edf-4c81-8d25-a2b03e33ab39)


### 4.Build and Push Docker Images

You can do it via gha workflow given -
![image](https://github.com/user-attachments/assets/b6ad5bb3-9e20-40a2-abd7-45d4f63c1fd4)

![image](https://github.com/user-attachments/assets/6522dab6-50d0-4fc6-983c-3146dc465e94) --https://github.com/Harithasridhar1306/terraform-github-mcp/actions/runs/15823257306/job/44597154118

Inoder to run this workflow you need to give you Docker username and DOcker Password(not recommended) please use PAT instead --under variables & Secrets
![image](https://github.com/user-attachments/assets/ae8d38f7-2bde-41bd-a9ab-cfed8d773a03)


docker build -t <your-docker-name>/users-service ./services/users
docker tag users-service <your-docker-name>/users-service:latest
docker push <your-docker-name>/users-service 
Later this docker image needs to be pushed to GCR.

### 5. Deploy to GKE with kubectl
gcloud container clusters get-credentials devops-cluster --region us-central1
kubectl apply -f k8s/users-deployment.yaml
kubectl apply -f k8s/users-service.yaml
