from utils import clean_name


def calculate_compatibility(name1: str, name2: str) -> tuple[int, str]:
    """
    Core logic:
    1. Convert names to lists of characters
    2. Remove common letters
    3. Calculate remaining letters
    4. Generate percentage and message
    """
    # Clean the names
    n1 = clean_name(name1)
    n2 = clean_name(name2)

    # Convert to lists (arrays)
    list1 = list(n1.replace(" ", ""))
    list2 = list(n2.replace(" ", ""))

    # Create temporary copies so we can safely remove items
    temp1 = list1.copy()
    temp2 = list2.copy()

    # Remove common letters
    for letter in list1:
        if letter in temp2:
            temp1.remove(letter)
            temp2.remove(letter)

    # Count remaining letters
    remaining = len(temp1) + len(temp2)

    # Calculate percentage (simple beginner-friendly formula)
    if remaining == 0:
        percentage = 100
    else:
        percentage = max(15, 100 - (remaining * 8))
        if percentage > 100:
            percentage = 100

    # Generate friendly message
    if percentage >= 85:
        message = "Best Friends Forever! 💛"
    elif percentage >= 70:
        message = "Great Friendship! 😊"
    elif percentage >= 50:
        message = "Good Friends 👍"
    elif percentage >= 30:
        message = "Getting to Know Each Other 🌱"
    else:
        message = "Just Acquaintances 🤝"

    return percentage, message
