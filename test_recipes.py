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
    