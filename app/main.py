from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Session, select
from app.models import Cliente, ClienteCreate, ClienteRead
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

# (CREATE/POST) Endpoint para cadastrar um novo cliente
@app.post("/clientes", response_model=ClienteRead)
def criar_cliente(cliente: ClienteCreate, session: Session = Depends(get_session)):
    novo = Cliente(**cliente.model_dump())
    session.add(novo)
    session.commit()
    session.refresh(novo)
    return novo

# (READ/GET) Endpoint para listagem de cliente(s)
@app.get("/clientes", response_model=List[ClienteRead])
def listar_clientes(session: Session = Depends(get_session)):
  results = session.exec(select(Cliente)).all()
  return results