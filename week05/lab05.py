def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid.

    Each user is a dictionary that may have an "age" key.
    Users with no age, or an age that is not a number,
    are skipped.

    Args:
        users: A list of user dictionaries.

    Returns:
        The average of the valid ages as a float, or 0.0 if
        there are no valid ages.
    """
    valid_ages = []

    for user in users:
        age = user.get("age")
        # Keep only real numbers. bool is excluded because
        # Python treats True/False as 1/0.
        if isinstance(age, (int, float)) and not isinstance(age, bool):
            valid_ages.append(age)

    if not valid_ages:
        return 0.0

    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return email addresses belonging to active users.

    A user's email is included only when "is_active" is truthy
    and the user has an "email" key.

    Args:
        users: A list of user dictionaries.

    Returns:
        A list of email strings. It is empty if no active
        users have an email.
    """
    emails = []

    for user in users:
        if user.get("is_active") and "email" in user:
            emails.append(user["email"])

    return emails