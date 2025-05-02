from . import customer,payments, orders, order_details, recipes, menu_items, resources, feedback,  promotions
from ..dependencies.database import engine


def index():
    customer.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)