from . import orders, order_details, customers, payments, recipes, resources, promotions, menu_items, feedback

def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(payments.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
    app.include_router(promotions.router)
    app.include_router(menu_items.router)
    app.include_router(feedback.router)