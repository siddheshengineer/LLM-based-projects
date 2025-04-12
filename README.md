# Repository Overview

**[AI Research Agent](https://ai.siddheshnikam.online/)**

Welcome to the repository! This document provides an overview of the projects and files contained within.

## Projects and Directories

### 1. `Kaggel-googleGenAi-porjects/`

This directory contains projects related to Google's Generative AI, likely from a Kaggle competition or course.

**Files:**

- **README.md:**  Project-specific documentation.
- **day-1-evaluation-and-structured-output.ipynb:** Jupyter Notebook for evaluating and structuring outputs from generative AI models.
- **day-1-prompting.ipynb:**  Jupyter Notebook focusing on effective prompting techniques for generative AI models.
- **day-2-document-q-a-with-rag.ipynb:**  Jupyter Notebook implementing a document question-answering system using Retrieval-Augmented Generation (RAG).
- **day-2-embeddings-and-similarity-scores.ipynb:** Jupyter Notebook exploring embeddings and similarity scores in the context of generative AI.
- **day-3-building-an-agent-with-langgraph.ipynb:** Jupyter Notebook demonstrating the creation of an AI agent using LangGraph.
- **day-3-function-calling-with-the-gemini-api.ipynb:** Jupyter Notebook showcasing function calling capabilities with the Gemini API.
- **day-4-fine-tuning-a-custom-model.ipynb:** Jupyter Notebook detailing the process of fine-tuning a custom generative AI model.
- **day-4-google-search-grounding.ipynb:** Jupyter Notebook utilizing Google Search to ground or enhance the outputs of a generative AI model.

**Subdirectory:**

- **whitepapers/:** Contains relevant whitepapers as PDF documents:
    - 22365_19_Agents_v8.pdf
    - 22365_3_Prompt Engineering_v7.pdf
    - Agents_Companion_v2 (3).pdf
    - neurips_evaluation.pdf
    - whitepaper_Foundational Large Language models & text generation_v2.pdf
    - whitepaper_emebddings_vectorstores_v2.pdf

### 2. `composeToManifestScript/`

This directory includes scripts for converting Docker Compose configurations to Kubernetes manifests.

**Files:**

- **localScript.py:** Python script for local execution of the conversion process.
- **script.py:**  Main Python script to perform the conversion.

### 3. `contanerizationScript/`

This directory focuses on containerization, likely with scripts for generating Dockerfiles or managing containers.

**Files:**

- **hostedLLMScript.py:** Script designed to work with hosted Large Language Models (LLMs) for containerization tasks.
- **localScript.py:** Script for local containerization operations.

### 4. `memory-chatbot/`

Contains a chatbot implementation that incorporates memory capabilities to enable a choose your own adventure game.

**File:**

- **memory-bot.py:** Python script for the memory-enabled chatbot.

### 5. `agents/research_agent/`

This directory houses an implementation of a research agent, an AI agent designed to assist with research tasks.

**Files:**

- **Dockerfile:** Defines the Docker image for the research agent.
- **cleanup.py:**  Script for cleaning up resources or data related to the agent.
- **core.py:**  Core logic and functionality of the research agent.
- **deployment_instructions.md:** Instructions for deploying the research agent.
- **docker-compose.yml:** Docker Compose file for managing the agent's services and dependencies.
- **main.py:**  Entry point or main application file for running the agent.
- **requirements.txt:** Lists the Python dependencies required by the agent.
- **test_endpoints.py:**  Script for testing the agent's API endpoints.
- **tools.py:**  Contains tools used by the research agent.

**Subdirectory:**

- **templates/:** Contains HTML templates for the agent's web interface.
    - **index.html:** Main page template.
    - **result.html:** Template for displaying research results.
