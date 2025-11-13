# 🛡️ Robust FastAPI — API Resiliente e Monitorada com MongoDB

Projeto desenvolvido com o objetivo de demonstrar **boas práticas de desenvolvimento backend em Python**, utilizando **FastAPI**, **MongoDB** e **tratamento estruturado de erros e logs**.

A API simula um sistema real de **cadastro de usuários**, **criação de pedidos** e **upload de arquivos**, implementando um modelo de arquitetura robusto e preparado para lidar com falhas de forma controlada.

---

## 🚀 Tecnologias Utilizadas

| Camada | Tecnologias |
|--------|--------------|
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Banco de Dados** | [MongoDB](https://www.mongodb.com/) via `motor` |
| **Log & Monitoramento** | `logging`, logger customizado e alertas simulados (`core/monitor.py`) |
| **Validação e Configuração** | [Pydantic Settings + Models](https://docs.pydantic.dev/latest/) |
| **Testes (planejado)** | `pytest` + `httpx` |
| **Container (opcional)** | Docker |

---

## 🧩 Estrutura do Projeto

Robust-FastApi/
├── src/
│ ├── app/
│ │ ├── api/ # Rotas da aplicação
│ │ │ ├── users.py
│ │ │ ├── orders.py
│ │ │ └── uploads.py
│ │ ├── core/ # Configurações e componentes centrais
│ │ │ ├── config.py # Carrega variáveis do .env
│ │ │ ├── db.py # Conexão MongoDB
│ │ │ ├── logger.py # Sistema de logs
│ │ │ └── monitor.py # Alerta para erros críticos
│ │ ├── models/ # Schemas e modelos Pydantic
│ │ ├── services/ # Integrações externas simuladas
│ │ └── main.py # Ponto de entrada da API
│ └── .env # Variáveis de ambiente
├── requirements.txt
└── README.md

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o projeto
```bash
git clone https://github.com/seuusuario/robust-fastapi.git
cd robust-fastapi
```

### 2️⃣ Criar ambiente virtual
```bash
python -m venv venv
# Ativar (Windows)
venv\Scripts\activate
# Ativar (Linux/Mac)
source venv/bin/activate
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variáveis de ambiente
Crie o arquivo `.env` dentro da pasta `src/` com conteúdo exemplo:

```
MONGO_URI=mongodb://localhost:27017/robustdb
LOG_LEVEL=INFO
```

Dica: rode o MongoDB via Docker para testar facilmente:
```bash
docker run -d --name robust-mongo -p 27017:27017 mongo:6.0
```

### 5️⃣ Iniciar o servidor
```bash
cd src
uvicorn app.main:app --reload --port 8000
```

Acesse:
- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

---

## 🧪 Endpoints Principais

Usuários (/users)
- POST /users/ — Cria um novo usuário
- GET /users/ — Lista todos os usuários

Pedidos (/orders)
- POST /orders/ — Cria um novo pedido e simula pagamento externo
- GET /orders/ — Lista todos os pedidos criados

Uploads (/upload)
- POST /upload/ — Faz upload de arquivo e salva localmente

---

## 🧰 Recursos de Robustez Implementados

- Health Check: endpoint `/health` verifica o status da API e do banco de dados e retorna 503 em caso de degradação.
- Tratamento Global de Exceções: exceções são interceptadas por um handler global; erros são registrados e enviados ao monitor de alertas (`core/monitor.py`).
- Logs Estruturados: eventos relevantes são registrados em `robust.log` (INFO, WARNING, ERROR) com detalhes como rota e método HTTP.
- Injeção Dinâmica de Conexão: rotas acessam `core.db.db` dinamicamente para garantir que o banco só seja usado após inicialização completa.
- Integração com API Externa Simulada: `services/payment_client.py` representa uma API de pagamento real para testar falhas e tratamento resiliente.

---

## 📈 Próximos Passos

- Adicionar testes unitários e de integração com `pytest` e `httpx`.
- Implementar `get_db()` via `Depends()` (injeção de dependência FastAPI).
- Criar índice único no Mongo (email) e tratar `DuplicateKeyError`.
- Adicionar `Dockerfile` e `docker-compose` (API + Mongo + Logs).
- Integrar monitoramento real (Slack, SMTP ou webhook).

---

## 🧠 Intuito do Projeto

Demonstrar boas práticas backend com Python + FastAPI, resiliência, tratamento de erros e observabilidade — ideal para portfólio e aprendizado.

---

## 👨‍💻 Autor

Igorzon  
Desenvolvedor Python | Backend & APIs  
Contato: seu-email@exemplo.com  
LinkedIn: linkedin.com/in/seuusuario

---

## 🧭 Licença

Uso livre para fins de aprendizado e portfólio.

