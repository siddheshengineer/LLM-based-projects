# LLM-Based Containerization

Welcome to the **LLM-Based Containerization** repository! This project leverages **Large Language Models (LLMs)** to generate optimized Dockerfiles for various programming languages, ensuring best practices and efficiency.

##  Features
- **Automated Dockerfile Generation**: Uses `llama3.2:1b` model from `ollama` to generate Dockerfiles dynamically.
- **Google Gemini 2.0 Integration**: A new script leverages `Google Gemini 2.0` via `Google AI Studio` to generate Dockerfiles remotely.
- **Best Practices**: Ensures each Dockerfile includes an optimized base image, dependencies installation, workspace setup, and execution commands.
- **Multi-Language Support**: Generate Dockerfiles for different programming languages on demand. If no version is provide it will automatically use the latest LTS version available.

## 📦 Installation

To use this script, you need to have Python installed along with the required dependencies.

```sh
pip install -r requirements.txt
```

##  Usage

Run the script and input your desired programming language to generate a Dockerfile.

```sh
python localScript.py
python .\hostedLLM\hostedLLMScript.py

```

### Example:
Check generated_dockerFiles.md for generated examples

```
Enter the desired programming language: Java
Generated DockerFile: 

```dockerfile
# syntax=docker/dockerfile:1

# Stage 1: Build the application
FROM maven:3.8.1-openjdk-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B
COPY src ./src
RUN mvn clean install -DskipTests

# Stage 2: Create the final image
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```


##  How It Works
1. The script prompts the user to enter a programming language.
2. It passes a structured prompt to the `llama3.2:1b` model using `ollama.chat()` or `Google Gemini 2.0` via `Google AI Studio`.
3. The model generates an optimized Dockerfile based on best practices.
4. The output is displayed in the console.

##  Requirements
- Python 3.x
- `ollama` package
- google-generativeai package
- Google AI Studio API Key
- Internet connection to interact with the LLM model

##  Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions or bug reports.

##  Contact
For any queries or discussions, feel free to reach out via GitHub issues.

---

Happy Containerizing! 🐳

