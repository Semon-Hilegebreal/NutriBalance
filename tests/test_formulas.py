import pytest
from src.models.user import Gender, ActivityLevel
from src.utils.formulas import (
    calculate_bmr,
    calculate_tdee,
    calculate_bmi,
    calculate_macros
)


class TestBMR:
    
    def test_bmr_for_male(self):
        result = calculate_bmr(75, 180, 28, Gender.MALE)
        assert 1700 < result < 1800
    
    def test_bmr_for_female(self):
        result = calculate_bmr(62, 165, 25, Gender.FEMALE)
        assert 1300 < result < 1400
    
    def test_bmr_different_by_gender(self):
        male_bmr = calculate_bmr(70, 170, 30, Gender.MALE)
        female_bmr = calculate_bmr(70, 170, 30, Gender.FEMALE)
        assert male_bmr > female_bmr


class TestTDEE:
    
    def test_sedentary_multiplier(self):
        bmr = 1700
        tdee = calculate_tdee(bmr, ActivityLevel.SEDENTARY)
        assert tdee == 2040.0
    
    def test_active_multiplier(self):
        bmr = 1500
        tdee = calculate_tdee(bmr, ActivityLevel.ACTIVE)
        assert tdee == 2587.5


class TestBMI:
    
    def test_bmi_calculation(self):
        bmi = calculate_bmi(70, 175)
        assert 22 < bmi < 23
    
    def test_bmi_underweight(self):
        bmi = calculate_bmi(45, 170)
        assert bmi < 18.5


class TestMacros:
    
    def test_maintain_macros(self):
        macros = calculate_macros(2000, "maintain")
        assert macros["protein_g"] == 150
        assert macros["carbs_g"] == 200
        assert macros["fat_g"] == 67
    
    def test_weight_loss_macros(self):
        macros = calculate_macros(1500, "lose_weight")
        assert macros["protein_g"] == 150