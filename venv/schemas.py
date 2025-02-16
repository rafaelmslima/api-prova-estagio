from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int
    nome: str
    
    model_config = ConfigDict(from_attributes=True)

class ObrigacaoBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoCreate(ObrigacaoBase):
    pass

class ObrigacaoResponse(ObrigacaoBase):
    id: int
    class Config:
        from_attributes = True
