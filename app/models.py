from sqlmodel import SQLModel, Field
from typing import Optional

# Nova tabela no banco chamada 'cliente'
class Cliente(SQLModel, table=True):

  # ID inicial vazio (será gerado pelo banco)
  id: Optional[int] = Field(default=none, primary_key=True) 
  nome: str
  email: str
  cpf: str