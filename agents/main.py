from dotenv import dotenv_values
from pydantic import BaseModel
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
#from tools import search_tool, wiki_tool, save_tool

secrets = dotenv_values(".env")

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=secrets["GOOGLE_API_KEY"])

## Just for fun ##
# response = llm.invoke("What is the meaning of life?")
# print(response)

parser = PydanticOutputParser(pydantic_object = ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are research assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
            Wrap the output in this format and provide no other test \n{format_instructions}
            """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[]
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=False)

raw_response = agent_executor.invoke({"query":"Why is capital of Canada?"})

try: 
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
    #print(structured_response.summary)
except Exception as e:
    print("Error parsing output, ", e, "Raw response - \n", raw_response)





