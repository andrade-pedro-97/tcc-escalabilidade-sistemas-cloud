from fastapi import FastAPI
from sqlmodel import SQLModel
from app.models import Cliente
from app.database import engine
from contextlib import asynccontextmanager

# Liga com os eventos de "startup" e "shutdown"
@asynccontextmanager
async def lifespan(app: FastAPI):

  # Aplicação inicia -> roda abaixo
  SQLModel.metadata.create_all(engine)
  yield

app = FastAPI(lifespan=lifespan)