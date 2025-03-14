PS D:\Study\devops\GenAI\containerizationScript> python .\hostedLLM\hostedLLMScript.py
Enter the desired programming language: Java
Generated DockerFile: 

```dockerfile
# Multi-stage build for optimal image size

# Stage 1: Build the application
FROM maven:3.8.7-openjdk-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B
COPY src ./src
RUN mvn clean install -DskipTests

# Stage 2: Create the runtime image
FROM eclipse-temurin:17-jre-jammy
LABEL maintainer="Your Name <your.email@example.com>"

ARG UNAME=appuser
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID $UNAME && \
    useradd -u $UID -g $UNAME -m $UNAME

WORKDIR /app

COPY --from=builder /app/target/*.jar app.jar

USER $UNAME

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

PS D:\Study\devops\GenAI\containerizationScript> python .\hostedLLM\hostedLLMScript.py
Enter the desired programming language: nextjs
Generated DockerFile: 

```dockerfile
# Dockerfile
FROM node:18-alpine AS base

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Production image
FROM node:18-alpine AS production

# Set working directory
WORKDIR /app

# Copy production dependencies
COPY package*.json ./
RUN npm install --production

# Copy nextjs build output
COPY --from=base /app/.next ./.next
COPY --from=base /app/public ./public
COPY --from=base /app/next.config.js ./
COPY --from=base /app/next-i18next.config.js ./

# Add user
RUN addgroup -g 1001 nodejs
RUN adduser -u 1001 -G nodejs nextjs
USER nextjs

# Expose port
EXPOSE 3000

# Set environment variables
ENV NODE_ENV production

# Start the server
CMD ["npm", "start"]