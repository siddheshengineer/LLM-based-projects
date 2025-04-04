from dotenv import dotenv_values
import google.generativeai as genai

secrets = dotenv_values(".env")

genai.configure(api_key=secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')

# Multi line prompt, to specify the exact requirement (few-shot prompt)
PROMPT = """
ONLY Generate the ideal docker file for the {language} with best practices. Do not provide any description. If version is not mentioned use the latest LTS version.
Include:
- If applicable use multistage docker build
- BASE_IMAGE
- Dependencies installation
- Setting work directory
- Adding or copying source code
- Don't use root use, use docker best security practices.
- Running the application
"""
# Function to generate the docker file
def generateDockerFile(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text

# Call the function
if __name__ == '__main__':
    language = input("Enter the desired programming language: ")
    dockerFile = generateDockerFile(language)
    print("Generated DockerFile: \n")
    print(dockerFile)