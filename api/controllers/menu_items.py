from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models import menu_items as model
from ..schemas import menu_items as schema


def create(db: Session, request: schema.MenuItemCreate):
    new_item = model.MenuItem(
        item_name=request.item_name,
        price=request.price,
        calories=request.calories,
        order_category=request.order_category
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__['orig']))
    return new_item


def read_all(db: Session):
    try:
        return db.query(model.MenuItem).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__['orig']))


def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Menu item not found")
        return item
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__['orig']))


def update(db: Session, item_id: int, request: schema.MenuItemUpdate):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=404, detail="Menu item not found")
        item.update(request.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return item.first()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__['orig']))


def delete(db: Session, item_id: int):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=404, detail="Menu item not found")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__['orig']))

def get_items_by_category(db: Session, category: str):
    items = db.query(model.MenuItem).filter(model.MenuItem.order_category == category).all()
    if not items:
        raise HTTPException(status_code=404, detail="No items found for this category.")
    return items