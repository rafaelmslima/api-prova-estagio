from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas

app = FastAPI()

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

# Dependência de conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/empresas/", response_model=schemas.EmpresaResponse)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = models.Empresa(**empresa.model_dump())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/", response_model=list[schemas.EmpresaResponse])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()

@app.post("/obrigacoes/", response_model=schemas.ObrigacaoResponse)
def criar_obrigacao(obrigacao: schemas.ObrigacaoCreate, db: Session = Depends(get_db)):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/obrigacoes/", response_model=list[schemas.ObrigacaoResponse])
def listar_obrigacoes(db: Session = Depends(get_db)):
    return db.query(models.ObrigacaoAcessoria).all()

@app.get("/")
def read_root():
    return {"message": "API esta rodando corretamente!"}