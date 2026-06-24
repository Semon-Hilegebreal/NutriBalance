from dataclasses import dataclass
from typing import List
from enum import Enum


class FoodGroup(Enum):
    PROTEIN = "protein"
    GRAINS = "grains"
    VEGETABLES = "vegetables"
    FRUITS = "fruits"
    DAIRY = "dairy"
    FATS = "fats"


@dataclass
class NutritionInfo:
    calories: float
    protein_g: float
    carbs_g: float
    fat_g: float
    fiber_g: float = 0.0
    sugar_g: float = 0.0


@dataclass
class FoodItem:
    food_id: str
    name: str
    group: FoodGroup
    nutrition: NutritionInfo
    serving_g: float = 100.0

    def nutrition_for_grams(self, grams: float) -> NutritionInfo:
        ratio = grams / 100.0
        return NutritionInfo(
            calories=self.nutrition.calories * ratio,
            protein_g=self.nutrition.protein_g * ratio,
            carbs_g=self.nutrition.carbs_g * ratio,
            fat_g=self.nutrition.fat_g * ratio,
            fiber_g=self.nutrition.fiber_g * ratio,
            sugar_g=self.nutrition.sugar_g * ratio
        )


@dataclass
class Meal:
    name: str
    items: List[tuple]

    def total_nutrition(self) -> NutritionInfo:
        totals = NutritionInfo(0, 0, 0, 0, 0, 0)
        for food, grams in self.items:
            item_nut = food.nutrition_for_grams(grams)
            totals.calories += item_nut.calories
            totals.protein_g += item_nut.protein_g
            totals.carbs_g += item_nut.carbs_g
            totals.fat_g += item_nut.fat_g
            totals.fiber_g += item_nut.fiber_g
            totals.sugar_g += item_nut.sugar_g
        return totals
