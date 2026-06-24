from ..models.user import UserProfile, HealthGoal
from ..utils.formulas import calculate_bmr, calculate_tdee, calculate_macros, calculate_bmi


class NutritionCalculator:
    
    def get_daily_calories(self, user: UserProfile) -> float:
        bmr = calculate_bmr(user.weight_kg, user.height_cm, user.age, user.gender)
        tdee = calculate_tdee(bmr, user.activity_level)
        
        adjustments = {
            HealthGoal.LOSE_WEIGHT: -500,
            HealthGoal.GAIN_WEIGHT: 500,
            HealthGoal.MAINTAIN: 0,
            HealthGoal.HEART_HEALTH: -200,
            HealthGoal.DIABETES_CARE: -300
        }
        
        adjustment = adjustments.get(user.health_goal, 0)
        return round(tdee + adjustment, 2)
    
    def get_macro_targets(self, user: UserProfile) -> dict:
        calories = self.get_daily_calories(user)
        
        goal_map = {
            HealthGoal.LOSE_WEIGHT: "lose_weight",
            HealthGoal.MAINTAIN: "maintain",
            HealthGoal.GAIN_WEIGHT: "gain_weight",
            HealthGoal.HEART_HEALTH: "heart_health",
            HealthGoal.DIABETES_CARE: "diabetes_care"
        }
        
        goal_key = goal_map.get(user.health_goal, "maintain")
        return calculate_macros(calories, goal_key)
    
    def get_health_summary(self, user: UserProfile) -> dict:
        bmi = calculate_bmi(user.weight_kg, user.height_cm)
        category = user.get_bmi_category()
        
        warnings = []
        if bmi >= 30:
            warnings.append("Elevated BMI - consult healthcare provider")
        elif bmi >= 25:
            warnings.append("BMI slightly above normal range")
        
        risk_conditions = ["diabetes", "hypertension", "heart disease", "cholesterol"]
        for condition in user.conditions:
            if condition.lower() in risk_conditions:
                warnings.append(f"Managing: {condition}")
        
        return {
            "bmi": bmi,
            "category": category,
            "warnings": warnings,
            "status": "healthy" if len(warnings) == 0 else "needs_attention"
        } 
