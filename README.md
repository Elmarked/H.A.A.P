# Halo Azure Access Poke

Azure Function API that validates whether a user (UPN) has access to an Enterprise Application via group-based assignment.

## Features

- Scrapes UPN from Halo request
- Dynamically lists Enterprise Apps (assignment required)
- Validates group-based access
- Supports nested group membership
- Designed for Managed Identity
- Production-ready structure

## Endpoints

### GET /api/get-apps
Returns Enterprise Applications requiring assignment.

### POST /api/validate-access
Checks whether user has group-based access.

Request body:

{
  "upn": "user@company.com",
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx"
}

Response:

{
  "user": "user@company.com",
  "application": "Salesforce",
  "access": true,
  "matchedGroups": ["SG-Salesforce-Users"]
}

## Required Graph Permissions

- User.Read.All
- Group.Read.All
- AppRoleAssignment.Read.All
- Directory.Read.All

Admin consent required.# H.A.A.P
Halo Azure Application Poke
