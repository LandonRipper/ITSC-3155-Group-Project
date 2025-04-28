from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models import resources as model
from ..schemas import resources as schema


def create(db: Session, request: schema.ResourceCreate):
    new_resource = model.Resource(
        item=request.item,
        amount=request.amount
    )
    try:
        db.add(new_resource)
        db.commit()
        db.refresh(new_resource)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_resource


def read_all(db: Session):
    try:
        return db.query(model.Resource).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__["orig"]))


def read_one(db: Session, resource_id: int):
    try:
        resource = db.query(model.Resource).filter(model.Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")
        return resource
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__["orig"]))


def update(db: Session, resource_id: int, request: schema.ResourceUpdate):
    try:
        resource = db.query(model.Resource).filter(model.Resource.id == resource_id)
        if not resource.first():
            raise HTTPException(status_code=404, detail="Resource not found")
        resource.update(request.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return resource.first()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__["orig"]))


def delete(db: Session, resource_id: int):
    try:
        resource = db.query(model.Resource).filter(model.Resource.id == resource_id)
        if not resource.first():
            raise HTTPException(status_code=404, detail="Resource not found")
        resource.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__["orig"]))
