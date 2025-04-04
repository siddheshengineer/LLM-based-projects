from langchain.memory import ConversationBufferMemory
from langchain_google_genai import GoogleGenerativeAI
from langchain import LLMChain, PromptTemplate
from dotenv import dotenv_values
import json

secrets = dotenv_values(".env")

buff_memory = ConversationBufferMemory(
    memory_key="chat_history"
)

template = """
You are now the guide of a mystical journey in the Whispering Woods. 
A traveler named Elara seeks the lost Gem of Serenity. 
You must navigate her through challenges, choices, and consequences, 
dynamically adapting the tale based on the traveler's decisions. 
Your goal is to create a branching narrative experience where each choice 
leads to a new path, ultimately determining Elara's fate. 

Here are some rules to follow:
1. Start by asking the player to choose some kind of weapons that will be used later in the game
2. Have a few paths that lead to success
3. Have some paths that lead to death. If the user dies generate a response that explains the death and ends in the text: "The End.", I will search for this text to end the game

Here is the chat history, use this to understand what to say next: {chat_history}
Human: {human_input}
AI:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)


llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=secrets["G_API"])
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=buff_memory
)

choice = "start"

while True:
    response = llm_chain.predict(human_input=choice)
    print(response.strip())

    if "The End." in response:
        break

    choice = input("Your reply: ")