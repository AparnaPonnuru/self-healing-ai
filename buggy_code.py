def get_age_category(user):
    age = user.get('age', 0)
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 65:
        return "Adult"
    else:
        return "Senior"