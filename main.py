from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost/celulares_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# El resto del código permanece igual...

# Asegúrate de que todas las importaciones necesarias estén presentes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)