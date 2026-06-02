import pytest
from recipes import Ingredient,Recipe,ShoppingList,DietaryRecipe
def test_ingredient_init():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name=="Мука"
    assert ing.quantity==500.0
    assert ing.unit=="г"
def test_ingredient_quantity_is_float():
    ing=Ingredient("Мука", 500, "г")
    assert isinstance(ing.quantity,float)
def test_ingredient_quantity_negative():
    with pytest.raises(ValueError):
        Ingredient("Мука", -100, "г")
def test_ingredient_quantity_zero():
    with pytest.raises(ValueError):
        Ingredient("Мука", 0, "г")
def test_ingredient_str():
    ing=Ingredient("Мука", 500, "г")
    assert str(ing)=="Мука: 500.0 г"
def test_ingredient_eq_same():
    ing1=Ingredient("Мука", 500, "г")
    ing2=Ingredient("Мука", 200, "г")
    assert ing1==ing2
def test_ingredient_eq_different_name():
    ing1=Ingredient("Мука", 500, "г")
    ing2=Ingredient("Картофель", 500, "г")
    assert ing1!=ing2
def test_ingredient_eq_different_unit():
    ing1=Ingredient("Говядина", 500, "г")
    ing2=Ingredient("Говядина", 500, "кг")
    assert ing1!=ing2

def test_recipe_init():
    recipe=Recipe("Эчпочмак")
    assert recipe.title=="Эчпочмак"
    assert recipe.ingredients==[]
def test_recipe_add_ingredient():
    recipe=Recipe("Эчпочмак")
    ing=Ingredient("Мука", 500, "г")
    recipe.add_ingredient(ing)
    assert len(recipe)==1
def test_recipe_add_ingredient_duplicate():
    recipe=Recipe("Эчпочмак")
    recipe.add_ingredient(Ingredient("Мука", 300, "г"))
    recipe.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(recipe)==1
    assert recipe.ingredients[0].quantity==500.0
def test_recipe_scale_returns_new_object():
    recipe = Recipe("Эчпочмак")
    recipe.add_ingredient(Ingredient("Говядина", 400, "г"))
    scaled=recipe.scale(2)
    assert scaled is not recipe
def test_recipe_scale_quantity():
    recipe = Recipe("Эчпочмак")
    recipe.add_ingredient(Ingredient("Говядина", 400, "г"))
    scaled = recipe.scale(2)
    assert scaled.ingredients[0].quantity == 800.0
def test_recipe_scale_original_unchanged():
    recipe = Recipe("Эчпочмак")
    recipe.add_ingredient(Ingredient("Картофель", 300, "г"))
    recipe.scale(3)
    assert recipe.ingredients[0].quantity==300.0
def test_recipe_scale_invalid_ratio():
    recipe = Recipe("Эчпочмак")
    with pytest.raises(ValueError):
        recipe.scale(-1)
def test_recipe_scale_zero_ratio():
    recipe = Recipe("Эчпочмак")
    with pytest.raises(ValueError):
        recipe.scale(0)
def test_recipe_len():
    recipe = Recipe("Эчпочмак")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Говядина", 400, "г"))
    recipe.add_ingredient(Ingredient("Картофель", 300, "г"))
    recipe.add_ingredient(Ingredient("Лук репчатый", 150, "г"))
    recipe.add_ingredient(Ingredient("Сливочное масло", 100, "г"))
    assert len(recipe)==5

s