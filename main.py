from fastapi import FastAPI
from app.controllers.main import router
from app.models.database import init_db
import streamlit as st
from database import inicializar_banco

app = FastAPI(title="API Concessionaria Digital")

# Inicializa o banco no Neon
init_db()

app.include_router(router)
