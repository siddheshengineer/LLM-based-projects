import ollama # Import ollama package
from pathlib import Path

# Multi line prompt, to specify the exact requirement (few-shot prompt)
PROMPT = """
ONLY give the generated the ideal Kubernestes manisfest files one after the other (deployment, service and ay other related) as the output, for the {file} with best practices. Do not provide any description. If version is not mentioned use the latest LTS version.
Include:
- Don't use root use, use kubenetes best security practices.
- Running the application
"""
# Function to generate the docker file
def generateManisfestFiles(file):
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': PROMPT.format(file=file)}])
    return response['message']['content']

# Call the function
if __name__ == '__main__':
    file_path = input("Enter the desired Docker Compose file path: ")
    file = Path(file_path).read_text()
    manifest = generateManisfestFiles(file)
    print("Generated Kubernetes Manifests: \n")
    print(manifest)

    