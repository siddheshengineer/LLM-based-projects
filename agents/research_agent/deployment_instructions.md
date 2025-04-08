# Azure CLI command to create and manage Azure Container App

## Create Azure Resource Group
```bash
az group create --name $RG_NAME --location $REGION
```

## Create Azure container environment
```bash
az containerapp env create --name $ENV_NAME --resource-group $RG_NAME --location $REGION
```
# Create application instance of Azure Container App
```bash
az containerapp create \
  --name $APP_NAME \
  --resource-group $RG_NAME \
  --image $IMAGE:TAG \
  --target-port 8000 \
  --ingress 'external' \
  --environment '$ENV_NAME' \
  --registry-server index.docker.io \
  --registry-username $REG_USER \
  --registry-password $REG_TOKEN \
  --env-vars GOOGLE_API_KEY=$API_KEY \
  --query properties.configuration.ingress.fqdn
```
# Update scaling policy
```bash
az containerapp update \
    --name $APP_NAME \
    --resource-group $RG_NAME \
    --min-replicas 1 \
    --max-replicas 3 \
    --scale-rule-name my-http-scale-rule \
    --scale-rule-http-concurrency 4
```
# System logs
```bash
az containerapp logs show \
    --name $APP_NAME \
    --resource-group $RG_NAME \
    --type=system \
    --follow=true
```
# Settting up custom URL: 
```bash
az containerapp hostname add --hostname $CUST_HOST -g $RG_NAME -n $APP_NAME

az containerapp hostname bind --hostname $CUST_HOST -g $RG_NAME -n $APP_NAME \
> --environment llm-env --validation-method CNAME
```