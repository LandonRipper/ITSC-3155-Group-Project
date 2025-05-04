from sqlalchemy.orm import Session
from .models.menu_items import MenuItem
from .models.resources import Resource
from .models.recipes import Recipe

def seed_data(db: Session):
    if db.query(MenuItem).first():
        return

    # ========== MENU ITEMS ==========
    burger = MenuItem(
        item_name="Burger", price=8.99, calories=800, order_category="Entree"
    )
    salad = MenuItem(
        item_name="Salad", price=7.99, calories=600, order_category="Entree"
    )
    fries = MenuItem(
        item_name="Fries", price=3.49, calories=500, order_category="Side"
    )
    soda = MenuItem(
        item_name="Soda", price=1.99, calories=150, order_category="Beverage"
    )
    chicken_wrap = MenuItem(
        item_name="Chicken Wrap", price=9.49, calories=750, order_category="Entree"
    )

    # ========== RESOURCES ==========
    bread = Resource(item="Bread", amount=300)
    beef_patty = Resource(item="Beef Patty", amount=200)
    lettuce = Resource(item="Lettuce", amount=300)
    potato = Resource(item="Potato", amount=400)
    oil = Resource(item="Oil", amount=1000)  # measured in ml
    soda_syrup = Resource(item="Soda Syrup", amount=500)
    tortilla = Resource(item="Tortilla", amount=150)
    chicken = Resource(item="Chicken", amount=180)

    db.add_all([
        burger, salad, fries, soda, chicken_wrap,
        bread, beef_patty, lettuce, potato, oil, soda_syrup, tortilla, chicken
    ])
    db.commit()

    # ========== RECIPES ==========
    # - NEED TO CREATE A NEW ROW FOR EACH INGREDIENT USED
    burger_beef = Recipe(
        menu_item_id=burger.id,
        resource_id=beef_patty.id,
        amount=1,
        item_description="Burger",
        resource_description="Beef patty"
    )
    burger_bread = Recipe(
        menu_item_id=burger.id,
        resource_id=bread.id,
        amount=2,
        item_description="Burger",
        resource_description="Burger bun"
    )
    salad_lettuce = Recipe(
        menu_item_id=salad.id,
        resource_id=lettuce.id,
        amount=4,
        item_description="Salad",
        resource_description="Lettuce"
    )
    fries_recipe = Recipe(
        menu_item_id=fries.id,
        resource_id=potato.id,
        amount=3,
        item_description="Fries",
        resource_description="Potatoes"
    )
    fries_oil = Recipe(
        menu_item_id=fries.id,
        resource_id=oil.id,
        amount=20,
        item_description="Fries",
        resource_description="Frying oil"
    )
    soda_recipe = Recipe(
        menu_item_id=soda.id,
        resource_id=soda_syrup.id,
        amount=5,
        item_description="Soda",
        resource_description="Soda syrup"
    )
    wrap_tortilla = Recipe(
        menu_item_id=chicken_wrap.id,
        resource_id=tortilla.id,
        amount=1,
        item_description="Chicken Wrap",
        resource_description="Tortilla wrap"
    )
    wrap_chicken = Recipe(
        menu_item_id=chicken_wrap.id,
        resource_id=chicken.id,
        amount=1,
        item_description="Chicken Wrap",
        resource_description="Cooked chicken"
    )
    wrap_lettuce = Recipe(
        menu_item_id=chicken_wrap.id,
        resource_id=lettuce.id,
        amount=2,
        item_description="Chicken Wrap",
        resource_description="Lettuce"
    )

    db.add_all([
        burger_beef, burger_bread, salad_lettuce,
        fries_recipe, fries_oil,
        soda_recipe,
        wrap_tortilla, wrap_chicken, wrap_lettuce
    ])
    db.commit()
