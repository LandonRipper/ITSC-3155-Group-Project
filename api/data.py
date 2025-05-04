from sqlalchemy.orm import Session
from .models.menu_items import MenuItem
from .models.resources import Resource
from .models.recipes import Recipe

def seed_data(db: Session):
    if db.query(MenuItem).first():
        return
    #MENU ITEMS
    burger = MenuItem(
        item_name = "Burger",
        price = 8.99,
        calories = 800,
        order_category = "Entree"
    )
    salad = MenuItem(
        item_name = "Salad",
        price = 7.99,
        calories = 600,
        order_category = "Entree"
    )
    #RESOURCES
    bread = Resource(
        item = "Bread",
        amount = 200
    )
    beef_patty = Resource(
        item = "Beef Patty",
        amount = 100
    )
    lettuce = Resource(
        item = "Lettuce",
        amount = 150
    )

    db.add_all([burger, salad, beef_patty, lettuce, bread])
    db.commit()

    #RECIPIES - NEED TO CREATE A NEW ROW FOR EACH INGREDIENT USED
    burger_beef = Recipe(
        menu_item_id = burger.id,
        resource_id = beef_patty.id,
        amount = 1,
        item_description = "Burger",
        resource_description = "Beef patty"
    )
    burger_bread = Recipe(
        menu_item_id = burger.id,
        resource_id = bread.id,
        amount = 2,
        item_description = "Burger",
        resource_description = "Burger bun"
    )
    salad_lettuce = Recipe(
        menu_item_id = salad.id,
        resource_id = lettuce.id,
        amount = 4,
        item_description="Salad",
        resource_description="Lettuce"
    )

    db.add_all([burger_beef, burger_bread, salad_lettuce])
    db.commit()

