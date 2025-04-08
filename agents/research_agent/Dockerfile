# Arguments
ARG PYTHON_VERSION=3.9.21-alpine3.21

FROM python:${PYTHON_VERSION}
LABEL org.opencontainers.image.description="Project: LLM Reserach agent"

# runtime variables
ENV USER_NAME=secUser
ENV GROUP_NAME=secGroup
ENV USER_ID=8754
ENV GROUP_ID=4876
ENV APP_PORT=8000

# Custom user
RUN addgroup -g ${GROUP_ID} -S ${GROUP_NAME} && adduser -u ${USER_ID} -S ${USER_NAME} -G ${GROUP_NAME}

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .

# Change ownership
RUN chown -R ${USER_NAME}:${GROUP_NAME} /app

USER ${USER_NAME}

EXPOSE ${APP_PORT}
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]

