from dotenv import dotenv_values
import google.generativeai as genai
from pathlib import Path

secrets = dotenv_values(".env")

genai.configure(api_key=secrets["G_API"])
model = genai.GenerativeModel('gemini-2.0-flash')

# Multi line prompt, to specify the exact requirement (few-shot prompt)
PROMPT = """
ONLY give the generated the ideal Kubernestes manisfest files one after the other (deployment, service and ay other related) as the output, for the {file} with best practices. Do not provide any description. If version is not mentioned use the latest LTS version.
Include:
- Don't use root use, use kubenetes best security practices.
- Running the application
"""
# Function to generate the docker file
def generateManisfestFiles(file):
    response = model.generate_content(PROMPT.format(file=file))
    return response.text

# Call the function
if __name__ == '__main__':
    file_path = input("Enter the desired Docker Compose file path: ")
    file = Path(file_path).read_text()
    manifest = generateManisfestFiles(file)
    print("Generated Kubernetes Manifests: \n")
    print(manifest)

    