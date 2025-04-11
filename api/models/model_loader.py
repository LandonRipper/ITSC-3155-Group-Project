from . import orders, order_details, recipes, menu_items, resources, feedback, customer, promotions

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
