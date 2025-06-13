from sqlmodel import SQLModel, Field
from typing import Optional

# Nova tabela no banco chamada 'cliente'
class ClienteBase(SQLModel):
  nome: str
  email: str
  cpf: str

# ID inicial vazio (será gerado pelo banco)
class Cliente(ClienteBase, table=True):
  id: Optional[int] = Field(default=None, primary_key=True) 

class ClienteCreate(ClienteBase):
  pass

class ClienteRead(ClienteBase):
  id: int