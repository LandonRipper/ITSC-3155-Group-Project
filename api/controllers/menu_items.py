from sqlalchemy.orm import Session
from ..models.menu_items import MenuItems
from ..schemas.menu_items import MenuItemCreate, MenuItemUpdate
from sqlalchemy import exc

# Create a new menu item
def create_menu_item(db: Session, menu_item: MenuItemCreate):
    db_menu_item = MenuItems(**menu_item.dict())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

# Get a menu item by its ID
def get_menu_item(db: Session, menu_item_id: int):
    return db.query(MenuItems).filter(MenuItems.id == menu_item_id).first()

# Get all menu items
def get_menu_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MenuItems).offset(skip).limit(limit).all()

# Update a menu item by ID
def update_menu_item(db: Session, menu_item_id: int, menu_item: MenuItemUpdate):
    db_menu_item = db.query(MenuItems).filter(MenuItems.id == menu_item_id).first()
    if db_menu_item:
        for key, value in menu_item.dict(exclude_unset=True).items():
            setattr(db_menu_item, key, value)
        db.commit()
        db.refresh(db_menu_item)
    return db_menu_item

# Delete a menu item by ID
def delete_menu_item(db: Session, menu_item_id: int):
    db_menu_item = db.query(MenuItems).filter(MenuItems.id == menu_item_id).first()
    if db_menu_item:
        db.delete(db_menu_item)
        db.commit()
    return db_menu_item
