import pytest
from src.models.user import UserProfile, Gender, ActivityLevel, HealthGoal
from src.services.calculator import NutritionCalculator


@pytest.fixture
def test_user():
    return UserProfile(
        user_id="T001",
        name="Test",
        age=30,
        gender=Gender.FEMALE,
        weight_kg=65,
        height_cm=165,
        activity_level=ActivityLevel.MODERATE,
        health_goal=HealthGoal.MAINTAIN,
        allergies=[],
        conditions=[]
    )


def test_get_calories_returns_value(test_user):
    calc = NutritionCalculator()
    calories = calc.get_daily_calories(test_user)
    assert calories > 0


def test_get_macros_has_all_keys(test_user):
    calc = NutritionCalculator()
    macros = calc.get_macro_targets(test_user)
    assert "protein_g" in macros
    assert "carbs_g" in macros
    assert "fat_g" in macros


def test_health_summary_has_bmi(test_user):
    calc = NutritionCalculator()
    summary = calc.get_health_summary(test_user)
    assert summary["bmi"] > 0
    assert summary["status"] in ["healthy", "needs_attention"]


def test_weight_loss_reduces_calories(test_user):
    calc = NutritionCalculator()
    maintain_cals = calc.get_daily_calories(test_user)
    
    test_user.health_goal = HealthGoal.LOSE_WEIGHT
    loss_cals = calc.get_daily_calories(test_user)
    
    assert loss_cals < maintain_cals 
