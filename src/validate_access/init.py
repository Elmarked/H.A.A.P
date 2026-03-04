import azure.functions as func
import json
from ..shared.graph_client import graph_get
from ..shared.models import format_access_response

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        upn = body.get("upn")
        app_id = body.get("appId")

        # Get user
        user = graph_get(f"/users/{upn}")
        user_id = user["id"]

        # Get transitive groups
        user_groups = graph_get(
            f"/users/{user_id}/transitiveMemberOf/microsoft.graph.group"
        )["value"]

        # Get service principal
        sp = graph_get(
            f"/servicePrincipals?$filter=appId eq '{app_id}'"
        )["value"][0]

        # Get app assigned groups
        assignments = graph_get(
            f"/servicePrincipals/{sp['id']}/appRoleAssignedTo"
        )["value"]

        app_groups = [
            a for a in assignments if a["principalType"] == "Group"
        ]

        user_group_ids = {g["id"] for g in user_groups}
        matched_groups = [
            g["principalDisplayName"]
            for g in app_groups
            if g["principalId"] in user_group_ids
        ]

        access = len(matched_groups) > 0

        response = format_access_response(
            upn,
            sp["displayName"],
            access,
            matched_groups
        )

        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
