from ..models.user import Gender, ActivityLevel


def calculate_bmr(weight_kg: float, height_cm: float, age: int, gender: Gender) -> float:
    base = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)
    
    if gender == Gender.MALE:
        return round(base + 5, 2)
    else:
        return round(base - 161, 2)


def get_activity_multiplier(level: ActivityLevel) -> float:
    values = {
        ActivityLevel.SEDENTARY: 1.2,
        ActivityLevel.LIGHT: 1.375,
        ActivityLevel.MODERATE: 1.55,
        ActivityLevel.ACTIVE: 1.725,
        ActivityLevel.VERY_ACTIVE: 1.9
    }
    return values[level]


def calculate_tdee(bmr: float, activity: ActivityLevel) -> float:
    multiplier = get_activity_multiplier(activity)
    return round(bmr * multiplier, 2)


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def calculate_macros(calories: float, goal: str) -> dict:
    distributions = {
        "lose_weight": (0.40, 0.30, 0.30),
        "maintain": (0.30, 0.40, 0.30),
        "gain_weight": (0.25, 0.45, 0.30),
        "heart_health": (0.25, 0.50, 0.25),
        "diabetes_care": (0.30, 0.35, 0.35)
    }
    
    protein_pct, carbs_pct, fat_pct = distributions.get(goal, (0.30, 0.40, 0.30))
    
    return {
        "protein_g": round((calories * protein_pct) / 4),
        "carbs_g": round((calories * carbs_pct) / 4),
        "fat_g": round((calories * fat_pct) / 9)
    } 
