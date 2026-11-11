# 🧠 Project SOMA — Backend

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.1.0%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.54.0%2B-499848.svg?logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![Managed with uv](https://img.shields.io/badge/package%20manager-uv-de5fe9.svg?logo=astral&logoColor=white)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> The high-performance API server and core intelligence engine powering **Project SOMA** — an extensible AI workstation.

---

## 🌟 Overview

**Project SOMA** (Synthetic Operator & Memory Assistant) is a next-generation AI workstation crafted to unify conversational intelligence, model orchestration, automated workflows, and developer tooling into a cohesive environment.

This repository hosts the **SOMA Backend**, serving as the central nervous system for the workstation. It handles:
- **Client & Workstation Communication:** Delivering fast, low-latency REST and streaming APIs to desktop, web, or CLI frontends.
- **LLM Orchestration:** Managing local inference runtimes and cloud model providers.
- **Agent Execution & Workflows:** Coordinating tools, agents, and workspace context.
- **Extensible Architecture:** Modular service structure designed for rapid scaling and plugin integration.

---

## 🏛️ Architecture & Project Structure

The codebase is organized modularly to decouple API routing, configuration management, and external service interactions:

```text
.
├── .agents/               # Agent skill profiles and automation configurations
├── app/
│   ├── api/               # API route definitions and request/response schemas
│   │   ├── __init__.py
│   │   └── routes.py      # Extended route handlers and sub-routers
│   ├── core/              # Global application configuration and settings
│   │   ├── __init__.py
│   │   └── config.py      # Environment variables and config management
│   ├── services/          # Core business logic and external integrations
│   │   ├── __init__.py
│   │   └── llm.py         # LLM connectors, prompt templates, and streaming handlers
│   ├── __init__.py
│   └── main.py            # FastAPI application entrypoint and ASGI setup
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Deterministic dependency lockfile
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- **Python:** `3.14` or higher
- **Package Manager:** [`uv`](https://github.com/astral-sh/uv) (recommended) or standard `pip`

### 1. Clone the Repository

```bash
git clone https://github.com/zenvavaday-cell/SOMA-backend.git
cd SOMA-backend
```

### 2. Environment Setup

Using [`uv`](https://github.com/astral-sh/uv) for lightning-fast virtual environment creation and dependency sync:

```bash
# Create virtual environment and install dependencies
uv sync
```

Alternatively, with standard `venv` and `pip`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Run the Development Server

Start the local server with hot reload enabled:

```bash
# Using uv
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Or inside an activated virtualenv
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The server will be accessible at:
- **Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive OpenAPI Docs (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative API Docs (ReDoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Endpoints

### 1. Health Check
Checks if the SOMA backend server is running and healthy.

- **Method:** `GET`
- **Path:** `/`
- **Response:**
  ```json
  {
    "status": "active",
    "message": "SOMA backend is online"
  }
  ```

*Example request:*
```bash
curl -X GET http://127.0.0.1:8000/
```

---

### 2. Chat & Interaction
Dispatches messages to the SOMA processing pipeline.

- **Method:** `POST`
- **Path:** `/chat`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "message": "Hello SOMA, initialize workspace."
  }
  ```
- **Response:**
  ```json
  {
    "response": "Echo from SOMA: Hello SOMA, initialize workspace."
  }
  ```

*Example request:*
```bash
curl -X POST http://127.0.0.1:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello SOMA"}'
```

---

## 🗺️ Roadmap

- [ ] **Streaming Responses (SSE / WebSockets):** Real-time token streaming for chat generation.
- [ ] **Multi-Provider LLM Service (`app/services/llm.py`):** Pluggable providers (Local Ollama/vLLM, OpenAI, Anthropic, Gemini).
- [ ] **Agentic Tool Calling & Memory:** Semantic search, vector memory integration, and file system tools.
- [ ] **Authentication & Security:** API token verification and role-based permissions for multi-device workstations.
- [ ] **Telemetry & Logging:** Structured traces and request logging for debugging workflows.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to extend SOMA:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'feat: add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

