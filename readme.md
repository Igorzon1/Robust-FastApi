# Robust FastAPI — API Resiliente, Testada e Monitorada com MongoDB

API backend desenvolvida para simular um ambiente real de produção, aplicando boas práticas de arquitetura, testes automatizados, observabilidade e tratamento estruturado de erros.

O projeto simula um sistema completo com cadastro de usuários, criação de pedidos, upload de arquivos e integração externa mockada, priorizando manutenibilidade, confiabilidade e organização de código.

---

## 🧩 O problema que este projeto resolve
Projetos iniciantes normalmente ignoram:
- monitoramento
- logs
- tratamento de exceções
- testes automatizados
- simulação de falhas reais

Este sistema foi criado para simular **como uma API backend funciona em produção**, lidando com falhas, integrações externas e controle de erros — e não apenas "endpoints que funcionam".

---

## 🚀 Tecnologias Utilizadas

| Camada | Tecnologias |
|--------|-------------|
| Backend | FastAPI |
| Banco de dados | MongoDB (`motor`) |
| Testes | Pytest + HTTPX |
| Logs | logging + logger customizado |
| Monitoramento | Sistema de alerta (`core/monitor.py`) |
| Validação | Pydantic |
| Container (Opcional) | Docker |

---

## ✅ Funcionalidades

- Cadastro e gestão de usuários  
- Criação e listagem de pedidos  
- Upload de arquivos  
- Health check automatizado  
- Tratamento global de exceções  
- Logs estruturados  
- Monitoramento de falhas críticas  
- Integração externa simulada (ex: pagamento)  
- Testes automatizados assíncronos  

---

## 🏗️ Arquitetura e Estrutura

```
src/
 └── app/
     ├── api/         # Rotas da aplicação
     ├── core/        # Configurações e serviços centrais
     ├── models/      # Schemas Pydantic
     ├── services/    # Integrações externas simuladas
     └── main.py      # Ponto de entrada
 └── tests/           # Testes automatizados
```

A arquitetura é organizada para:
- manter baixo acoplamento  
- facilitar testes  
- permitir escalabilidade  
- centralizar erros e logs  
- isolar integração externa  

---

## ▶️ Como rodar o projeto localmente

### 1️⃣ Clonar repositório
```bash
git clone https://github.com/seuusuario/robust-fastapi.git
cd robust-fastapi
```

---

### 2️⃣ Criar ambiente virtual
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar variáveis de ambiente
Crie o arquivo `src/.env`:

```env
MONGO_URI=mongodb://localhost:27017/robustdb
LOG_LEVEL=INFO
```

💡 Dica: subir MongoDB via Docker:
```bash
docker run -d --name robust-mongo -p 27017:27017 mongo:6.0
```

---

### 5️⃣ Rodar API
```bash
cd src
uvicorn app.main:app --reload --port 8000
```

---

### 🌐 Endpoints disponíveis

Swagger:
```
http://127.0.0.1:8000/docs
```

Health:
```
http://127.0.0.1:8000/health
```

---

## 🧪 Executando os testes

### Configurar PATH:
Windows:
```powershell
$env:PYTHONPATH="src"
```

Linux/Mac:
```bash
export PYTHONPATH=src
```

---

### Rodar testes:
```bash
pytest -q
```

Testes cobrem:
- criação de usuários
- validação de duplicidade
- fluxo de pedidos
- falhas externas
- comportamento assíncrono
- retornos HTTP

---

## 🧠 Destaques Técnicos

### ✔ Health Check Automático
- Verifica conexão com MongoDB  
- Retorna `503` automaticamente em falhas  

---

### ✔ Middleware global de exceções
- Nenhuma exceção vaza diretamente  
- Logs técnicos + resposta amigável  

---

### ✔ Logs estruturados
Incluem:
- nível
- rota
- método
- mensagem detalhada  

Arquivo: `robust.log`

---

### ✔ Simulação de integração externa
O serviço simula:
- sucesso  
- timeout  
- falha  
- mocks nos testes  

Isso aproxima o sistema de cenários reais de produção.

---

### ✔ Testes automatizados
Utilizados para validar:
- regras de negócio  
- falhas controladas  
- exceções  
- concorrência  

---

## 📈 Próximos passos planejados

- Testes para upload  
- Índices e constraints no MongoDB  
- Dockerfile e docker-compose  
- Middleware de Request ID  
- Rate limiting  
- Exportação de logs (OpenTelemetry)  

---

## 👨‍💻 Autor

**Igorzon**  
Desenvolvedor Backend Python  
FastAPI | APIs REST | Arquitetura Limpa  

---

## 🧭 Licença
Uso livre para portfólio e fins educacionais.
