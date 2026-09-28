def is_valid_name(name: str) -> bool:
    """
    Check if the name is not empty and contains only letters and spaces.
    """
    if not name or not name.strip():
        return False

    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def validate_names(name1: str, name2: str) -> tuple[bool, str]:
    """
    Validate both names.
    Returns (is_valid, error_message)
    """
    if not is_valid_name(name1):
        return False, "Please enter a valid first name (only letters allowed)."

    if not is_valid_name(name2):
        return False, "Please enter a valid second name (only letters allowed)."

    return True, ""
