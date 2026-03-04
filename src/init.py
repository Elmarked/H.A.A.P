import azure.functions as func
import json
from ..shared.graph_client import graph_get

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        apps = graph_get(
            "/servicePrincipals?$filter=appRoleAssignmentRequired eq true"
        )

        results = []
        for app in apps.get("value", []):
            results.append({
                "name": app["displayName"],
                "appId": app["appId"]
            })

        return func.HttpResponse(
            json.dumps(results),
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
