from .models.user import UserProfile, Gender, ActivityLevel, HealthGoal
from .services.calculator import NutritionCalculator


def display_separator():
    print("=" * 50)


def display_header():
    display_separator()
    print("NUTRIBALANCE")
    print("Daily Nutrition Tracker & Meal Planner")
    display_separator()


def display_user_info(user: UserProfile):
    print(f"\nUser: {user.name}")
    print(f"Age: {user.age} | Gender: {user.gender.value}")
    print(f"Weight: {user.weight_kg}kg | Height: {user.height_cm}cm")
    print(f"Activity: {user.activity_level.value}")
    print(f"Goal: {user.health_goal.value}")


def display_targets(calculator: NutritionCalculator, user: UserProfile):
    calories = calculator.get_daily_calories(user)
    macros = calculator.get_macro_targets(user)
    
    print(f"\nDaily Targets:")
    print(f"  Calories: {calories} kcal")
    print(f"  Protein:  {macros['protein_g']}g")
    print(f"  Carbs:    {macros['carbs_g']}g")
    print(f"  Fat:      {macros['fat_g']}g")


def display_health(calculator: NutritionCalculator, user: UserProfile):
    health = calculator.get_health_summary(user)
    
    print(f"\nHealth Summary:")
    print(f"  BMI: {health['bmi']} ({health['category']})")
    print(f"  Status: {health['status']}")
    
    if health['warnings']:
        print(f"  Notes:")
        for warning in health['warnings']:
            print(f"    - {warning}")


def main():
    display_header()
    
    calculator = NutritionCalculator()
    
    user = UserProfile(
        user_id="U001",
        name="Sarah",
        age=32,
        gender=Gender.FEMALE,
        weight_kg=68,
        height_cm=167,
        activity_level=ActivityLevel.MODERATE,
        health_goal=HealthGoal.HEART_HEALTH,
        allergies=["peanuts"],
        conditions=["hypertension"]
    )
    
    display_user_info(user)
    display_targets(calculator, user)
    display_health(calculator, user)
    
    print(f"\nTip: Regular nutrition tracking helps maintain long-term health.")
    display_separator()


if __name__ == "__main__":
    main() 
