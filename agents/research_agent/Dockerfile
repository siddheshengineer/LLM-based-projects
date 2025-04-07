ARG PYTHON_VERSION=3.9.21-alpine3.21
FROM python:${PYTHON_VERSION} AS build

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt