from fastapi import APIRouter, Depends, HTTPException, status
from ..controllers.menu_items import create_menu_item, get_menu_item, get_menu_items, update_menu_item, delete_menu_item
from ..schemas.menu_items import MenuItemCreate, MenuItemUpdate
from sqlalchemy.orm import Session
from ..dependencies.database import get_db

router = APIRouter()

# Create a new menu item
@router.post("/menu_items/", response_model=MenuItemCreate, status_code=status.HTTP_201_CREATED)
def create(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    return create_menu_item(db=db, menu_item=menu_item)

# Get a menu item by ID
@router.get("/menu_items/{menu_item_id}", response_model=MenuItemCreate)
def read(menu_item_id: int, db: Session = Depends(get_db)):
    db_menu_item = get_menu_item(db=db, menu_item_id=menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    return db_menu_item

# Get all menu items
@router.get("/menu_items/", response_model=list[MenuItemCreate])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_menu_items(db=db, skip=skip, limit=limit)

# Update a menu item by ID
@router.put("/menu_items/{menu_item_id}", response_model=MenuItemCreate)
def update(menu_item_id: int, menu_item: MenuItemUpdate, db: Session = Depends(get_db)):
    db_menu_item = update_menu_item(db=db, menu_item_id=menu_item_id, menu_item=menu_item)
    if db_menu_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    return db_menu_item

# Delete a menu item by ID
@router.delete("/menu_items/{menu_item_id}", response_model=MenuItemCreate)
def delete(menu_item_id: int, db: Session = Depends(get_db)):
    db_menu_item = delete_menu_item(db=db, menu_item_id=menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    return db_menu_item
