from fastapi.testclient import TestClient
from main import app
import random

client = TestClient(app)

def gerar_cnpj_aleatorio():
  raiz = [random.randint(0,9) for _ in range(8)]
  sufixo = [0,0,0,1]

  dv = [random.randint(0,9), random.randint(0,9)]

  return f"{raiz[0]}{raiz[1]}.{raiz[2]}{raiz[3]}{raiz[4]}.{raiz[5]}{raiz[6]}{raiz[7]}/"\
         f"{sufixo[0]}{sufixo[1]}{sufixo[2]}{sufixo[3]}-{dv[0]}{dv[1]}" 

def test_criar_empresa():
  response = client.post("/empresas/", json={
    "nome": "Teste Automatizado 3",
    "cnpj": gerar_cnpj_aleatorio(),
    "endereco": "Rua das ruas, 504",
    "email": "teste@teste.com",
    "telefone": "4002-8922"
  })
  assert response.status_code == 200 #Verifica se a requisicao foi bem sucedida
  assert response.json()["nome"] == "Teste Automatizado 3"

def test_testar_empresas():
  response = client.get("/empresas/")
  assert response.status_code == 200 # Verifica se o GET funciona
  assert isinstance(response.json(), list) #Verifica se o retorno e uma lista

def test_criar_obrigacao():
  response = client.post("/obrigacoes/", json={
    "nome": "Testando obrigacoes",
    "periodicidade": "mensal",
    "empresa_id": 1
     }) 
  assert response.status_code == 200
  assert response.json()["nome"] == "Testando obrigacoes"