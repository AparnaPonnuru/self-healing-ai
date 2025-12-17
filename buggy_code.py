def get_user_name(user):
    if user.get("name") is None:
        return "Guest"
    return user["name"] if user["name"] else "Guest"