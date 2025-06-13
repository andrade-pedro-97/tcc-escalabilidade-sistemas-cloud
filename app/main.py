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

# (READ/GET) Endpoint para listagem de todos os cliente(s)
@app.get("/clientes", response_model=List[ClienteRead])
def listar_clientes(session: Session = Depends(get_session)):
  results = session.exec(select(Cliente)).all()
  return results

# (READ/GET) Endpoint para consulta unitária de cliente
@app.get("/cliente/{cliente_id}", response_model=ClienteRead)
def buscar_cliente(cliente_id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

# 
@app.put("/clientes/{cliente_id}", response_model=ClienteRead)
def atualizar_cliente(cliente_id: int, dados: ClienteCreate, session: Session = Depends(get_session)):
   cliente = session.get(Cliente, cliente_id)
   if not cliente:
      raise HTTPException(status_code=404, detail="Cliente não encontrado")
   
   cliente.nome = dados.nome
   cliente.email = dados.email
   cliente.cpf = dados.cpf

   session.add(cliente)
   session.commit()
   session.refresh(cliente)
   return cliente