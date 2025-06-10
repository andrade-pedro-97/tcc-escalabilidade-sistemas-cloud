from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session
from app.models import Cliente
from app.database import engine, get_session
from contextlib import asynccontextmanager
from typing import List

# Inicia a aplicação (cria tabelas no banco)
@asynccontextmanager
async def lifespan(app: FastAPI):

  # Aplicação inicia -> roda abaixo
  SQLModel.metadata.create_all(engine)
  yield

# Inicializa o FastAPI
app = FastAPI(lifespan=lifespan)

# Endpoint para cadastrar um novo cliente
@app.post("/clientes", response_model=Cliente)
def criar_cliente(cliente: Cliente, session: Session = Depends(get_session)):
  session.add(cliente)
  session.commit()
  session.refresh(cliente)
  return cliente