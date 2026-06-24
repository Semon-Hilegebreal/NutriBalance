def validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise ValueError("Age must be a whole number")
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return True


def validate_weight(weight_kg: float) -> bool:
    if not isinstance(weight_kg, (int, float)):
        raise ValueError("Weight must be a number")
    if weight_kg < 2 or weight_kg > 500:
        raise ValueError("Weight must be between 2 and 500 kg")
    return True


def validate_height(height_cm: float) -> bool:
    if not isinstance(height_cm, (int, float)):
        raise ValueError("Height must be a number")
    if height_cm < 40 or height_cm > 280:
        raise ValueError("Height must be between 40 and 280 cm")
    return True
