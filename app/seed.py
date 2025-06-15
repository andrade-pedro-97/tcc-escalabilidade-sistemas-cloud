from sqlmodel import Session, select, SQLModel
from sqlalchemy import text
from app.models import Cliente
from app.database import engine
from faker import Faker

faker = Faker('pt_BR')

emails_gerados = set()
cpfs_gerados = set()

def gerar_email_unico():
  while True:
    email = faker.unique.email()
    if email not in emails_gerados:
      emails_gerados.add(email)
      return email

def gerar_cpf_unico():
  while True:
    cpf = faker.unique.cpf()
    if cpf not in cpfs_gerados:
      cpfs_gerados.add(cpf)
      return cpf

def popular_banco(qtd=1000):
  print(f"Limpando base de dados...")
  SQLModel.metadata.create_all(engine)
  with Session(engine) as session:
    session.exec(text("DELETE FROM cliente")) # Reseta a tabela
    session.commit()

    print(f"Gerando {qtd} clientes fictícios...")
    for _ in range(qtd):
      cliente = Cliente(
          nome=faker.name(),
          email=gerar_email_unico(),
          cpf=gerar_cpf_unico()
      )
      session.add(cliente)

    session.commit()
    print(f"{qtd} clientes criados com sucesso!")

if __name__ == "__main__":
  popular_banco()