from dataclasses import dataclass
from typing import List
from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class ActivityLevel(Enum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    MODERATE = "moderate"
    ACTIVE = "active"
    VERY_ACTIVE = "very_active"


class HealthGoal(Enum):
    LOSE_WEIGHT = "lose_weight"
    MAINTAIN = "maintain"
    GAIN_WEIGHT = "gain_weight"
    HEART_HEALTH = "heart_health"
    DIABETES_CARE = "diabetes_care"


@dataclass
class UserProfile:
    user_id: str
    name: str
    age: int
    gender: Gender
    weight_kg: float
    height_cm: float
    activity_level: ActivityLevel
    health_goal: HealthGoal
    allergies: List[str]
    conditions: List[str]

    def get_bmi(self) -> float:
        height_m = self.height_cm / 100
        return round(self.weight_kg / (height_m ** 2), 1)

    def get_bmi_category(self) -> str:
        value = self.get_bmi()
        if value < 18.5:
            return "Underweight"
        elif value < 25:
            return "Normal weight"
        elif value < 30:
            return "Overweight"
        else:
            return "Obese"