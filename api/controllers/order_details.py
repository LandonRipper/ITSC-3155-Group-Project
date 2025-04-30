from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_details as order_model
from ..models import recipes as recipe_model
from ..models import resources as resource_model



from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = order_model.OrderDetail(
        order_id=request.order_id,
        item_id=request.item_id,
        quantity=request.quantity
    )
    try:
        db.add(new_item)
        recipe_entries = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.menu_item_id == request.item_id).all()

        if not recipe_entries:
            raise HTTPException(status_code=404, detail="No recipe found for this menu item.")

        for recipe in recipe_entries:
            resource = db.query(resource_model.Resource).filter(resource_model.Resource.id == recipe.resource_id).first()

            if not resource:
                raise HTTPException(status_code=404, detail=f"Resource with ID {recipe.resource_id} not found.")

            required_amount = recipe.amount * request.quantity

            if resource.amount < required_amount:
                raise HTTPException(
                    status_code=400,
                    detail=f"Not enough {resource.item}. Needed: {required_amount}, Available: {resource.amount}"
                )

            resource.amount -= required_amount
            db.add(resource)





        db.commit()
        db.refresh(new_item)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(order_model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, order_id):
    try:
        item = db.query(order_model.OrderDetail).filter(order_model.OrderDetail.id == order_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, order_id, request):
    try:
        item = db.query(order_model.OrderDetail).filter(order_model.OrderDetail.id == order_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, order_id):
    try:
        item = db.query(order_model.OrderDetail).filter(order_model.OrderDetail.id == order_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
