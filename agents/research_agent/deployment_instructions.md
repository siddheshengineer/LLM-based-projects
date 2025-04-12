
# Azure Container App Deployment Guide

This guide provides all the necessary Azure CLI commands to deploy the LLM Research Agent to Azure Container Apps.

---

## Set Environment Variables

```bash
RG_NAME=research-gorup-name
REGION=eastus
ENV_NAME=container-env-name
APP_NAME=container-app-name
# REG_USER=container-registry-user (Done via CICD)
# REG_TOKEN=container-registry-token (Done via CICD)
# IMAGE=docker.io/$REG_USER/private_repo (Done via CICD)
# TAG=llm_research_agent-5  (Done via CICD)
# API_KEY=your_google_api_key (Done via CICD)
CUST_HOST=research.yourdomain.com
```

---

## Create Resource Group

```bash
az group create --name $RG_NAME --location $REGION
```

---

## Create Azure Container App Environment

```bash
az containerapp env create --name $ENV_NAME --resource-group $RG_NAME --location $REGION
```

---

## Create the App

```bash
az containerapp create \
  --name $APP_NAME \
  --resource-group $RG_NAME \
  --image $IMAGE:TAG \
  --target-port 8080 \
  --ingress 'external' \
  --environment $ENV_NAME \
  --registry-server index.docker.io \
  --registry-username $REG_USER \
  --registry-password $REG_TOKEN \
  --env-vars GOOGLE_API_KEY=$API_KEY \
  --query properties.configuration.ingress.fqdn
```

---

## Configure Auto-Scaling

```bash
az containerapp update \
    --name $APP_NAME \
    --resource-group $RG_NAME \
    --min-replicas 0 \
    --max-replicas 3 \
    --scale-rule-name my-http-scale-rule \
    --scale-rule-http-concurrency 4
```

---

## View Logs

```bash
az containerapp logs show \
    --name $APP_NAME \
    --resource-group $RG_NAME \
    --type=system \
    --follow=true
```

---

## Setup Custom Domain (Optional)

```bash
az containerapp hostname add --hostname $CUST_HOST -g $RG_NAME -n $APP_NAME

az containerapp hostname bind --hostname $CUST_HOST -g $RG_NAME -n $APP_NAME \
 --environment $ENV_NAME --validation-method CNAME
```

## Create Azure Login credentials - used by Github Actions
```bash
az ad sp create-for-rbac --name "{name}" \
  --role contributor \
  --scopes /subscriptions/{subscription-id}/resourceGroups/$RG_NAME \
  --sdk-auth
```