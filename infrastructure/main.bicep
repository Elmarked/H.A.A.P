param location string = resourceGroup().location
param functionName string

resource storage 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: '${functionName}storage'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: '${functionName}-plan'
  location: location
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
  }
}

resource function 'Microsoft.Web/sites@2022-09-01' = {
  name: functionName
  location: location
  kind: 'functionapp'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: plan.id
  }
}
