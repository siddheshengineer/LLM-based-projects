
# 🧠 LLM Research Agent
**[Application Link](https://ai.siddheshnikam.online/)**

This AI-powered Research Assistant is designed to help students, professionals, and researchers generate structured insights on any topic using advanced language models. Built with **FastAPI**, **LangChain**, **Docker**, and deployed via **Azure Container Apps**, it delivers fast and intelligent results in a user-friendly web interface.

---

## Features

- 🔍 Topic research via AI (Gemini)
- 🌐 Web scraping DuckDuckGo & Wikipedia via tools
- 📄 Structured summaries and file downloads
- 🧪 API & UI endpoints with testing
- ☁️ Scalable cloud deployment (Azure Container Apps)
- 🛡️ Security-hardened Docker setup with vulnerability scanning

---

## Project Structure

```
agents/
└── research_agent/
    ├── main.py              # FastAPI entrypoint
    ├── core.py              # Agent orchestration logic
    ├── tools.py             # LangChain tools (search, wiki, save)
    ├── test_endpoints.py    # Unit tests
    ├── cleanup.py           # delete old files from container /download 
    ├── requirements.txt     # Dependencies
    ├── templates/           # HTML templates (Jinja2)
    └── downloads/           # Generated research files
```

---

## Local Development

```bash
cd agents/research_agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GOOGLE_API_KEY=your_gemini_api_key
uvicorn main:app --reload
```

Then visit: `http://localhost:8000`
---

## [Cloud Deployment Guide](./deployment_instructions.md)

## Containerized Run

```bash
docker build -t llm-research-agent .
docker run -e GOOGLE_API_KEY=your_key -p 8000:8000 llm-research-agent
```

---

## Secrets Required

| Name              | Description                |
|-------------------|----------------------------|
| `GOOGLE_API_KEY`  | Gemini API key for research |
| Docker Registry Login | For pulling image (Azure) |
| `AZURE_CREDENTIALS` | Service principal credentials |
| `AZURE_*` values   | App + resource config for CI/CD |

---

## CI/CD Pipeline

GitHub Actions automatically:
- ✅ Runs unit tests
- 🐳 Builds & scans Docker image (Trivy)
- 🔐 Pushes to Docker Hub (or GHCR)
- ☁️ Deploys to Azure Container App

---

## ⚠️ Legal Disclaimer

This tool provides AI-generated content and does not guarantee factual accuracy. Users are advised to verify results and avoid relying solely on this tool for critical research or decisions.

---
