def clean_name(name: str) -> str:
    """
    Remove extra spaces and convert to lowercase.
    """
    return name.strip().lower()


def format_result(name1: str, name2: str, percentage: int, message: str) -> str:
    """
    Format the final result string for display.
    """
    return (
        f"{name1.title()}  &  {name2.title()}\n\n"
        f"Friendship Score: {percentage}%\n\n"
        f"{message}"
    )
