import ollama # Import ollama package

# Multi line prompt, to specify the exact requirement (few-shot prompt)
PROMPT = """
ONLY Generate the ideal docker file for the {language} with best practices. Do not provide any description.
Include:
- BASE_IMAGE
- Dependencies installation
- Setting work directory
- Adding or copying source code
- Running the application
"""
# Function to generate the docker file
def generateDockerFile(language):
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': PROMPT.format(language=language)}])
    return response['message']['content']

# Call the function
if __name__ == '__main__':
    language = input("Enter the desired programming language: ")
    dockerFile = generateDockerFile(language)
    print("Generated DockerFile: \n")
    print(dockerFile)