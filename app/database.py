from sqlmodel import create_engine, Session

# URL para conexão com o banco de dados PostgreSQL (Uso local)
# TO DO -> trocar para a URL da AWS
# DATABASE_URL = "postgresql://postgres:123456@localhost:5432/meubanco"  -- Usado Localmente
DATABASE_URL = "postgresql://postgres:12345678@tcc-db.cwn2um4u0dye.us-east-1.rds.amazonaws.com:5432/postgres"

# Criação de motor de conexão com o banco
engine = create_engine(DATABASE_URL, echo=True)

# Função para criar uma sessão de uso do banco
def get_session():
  return Session(engine)