from fastapi import FastAPI


#import models
#from database import engine, SessionLocal, get_db
#from sqlalchemy.orm import Session
#from sqlalchemy import func

app = FastAPI()

@app.get("/")
async def root():
    return {"message": ""}