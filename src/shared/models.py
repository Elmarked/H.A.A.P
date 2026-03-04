def format_access_response(user, app_name, access, matched_groups):
    return {
        "user": user,
        "application": app_name,
        "access": access,
        "matchedGroups": matched_groups
    }
