# 🚀 API para Gestão de Empresas e Obrigações Acessórias

Esta API foi desenvolvida como parte da **Prova de Seleção de Estágio**, utilizando **FastAPI, SQLAlchemy, Pydantic e PostgreSQL** para gerenciar empresas e suas obrigações acessórias.

---

## 📜 **Índice**
- [📌 Funcionalidades](#-funcionalidades)
- [📦 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Como Configurar o Projeto](#️-como-configurar-o-projeto)
- [💻 Como Rodar a API](#-como-rodar-a-api)
- [🛠️ Como Testar a API](#️-como-testar-a-api)
- [📮 Endpoints Disponíveis](#-endpoints-disponíveis)
- [📄 Licença](#-licença)

---

## 📌 **Funcionalidades**
✅ Cadastro de empresas  
✅ Listagem de empresas  
✅ Cadastro de obrigações acessórias vinculadas às empresas  
✅ Listagem de obrigações acessórias  
✅ Testes unitários para validar a API  

---

## 📦 **Tecnologias Utilizadas**
- 🐍 **[Python 3.11](https://www.python.org/downloads/)**
- ⚡ **[FastAPI](https://fastapi.tiangolo.com/)**
- 🏛️ **[PostgreSQL](https://www.postgresql.org/)**
- 🔧 **[SQLAlchemy](https://www.sqlalchemy.org/)**
- 🏗️ **[Alembic](https://alembic.sqlalchemy.org/en/latest/)**
- ✅ **[Pytest](https://pytest.org/)** para testes automatizados

---

## ⚙️ **Como Configurar o Projeto**
### **1️⃣ Clonar o Repositório**
```sh
git clone https://github.com/rafaelmslima/api-prova-estagio
cd api-fastapi-estagio/venv

##2️⃣ *Criar um Ambiente Virtual*
python -m venv venv

##3️⃣ *Instalar as Dependências*
Ativar o ambiente virtual: venv\Scripts\activate
pip install -r requirements.txt

##4️⃣ *Criar e Configurar o Banco de Dados*
*Acesse o PostgreSQL e execute:*
CREATE DATABASE banco_estagio ENCODING 'UTF8';
CREATE USER admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE provaestagio TO admin;

*Crie o arquivo .env na raiz do projeto e adicione:*
DATABASE_URL=postgresql://admin:admin@localhost:5432/banco_estagio

##💻 *Como Rodar a API*
uvicorn main:app --reload

*A API estará rodando em:*
*👉 http://127.0.0.1:8000*

*Para acessar a documentação Swagger UI, entre em:*
*👉 http://127.0.0.1:8000/docs*

*Para acessar a documentação Redoc:*
*👉 http://127.0.0.1:8000/redoc*

##🛠️ *Como Testar a API*
###*Para rodar os testes unitários:*
pytest test_main.py
*Se todos os testes passarem, a saída será algo como:*
============================ 3 passed in 0.50s ============================
