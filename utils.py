def validate_bounds(minimum: int, maximum: int, value: int) -> bool:
    """Check if integer is between two other integers."""
    return minimum <= value <= maximum
