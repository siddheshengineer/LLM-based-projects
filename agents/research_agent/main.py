from dotenv import dotenv_values
#from pydantic import BaseModel
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
import json

secrets = dotenv_values(".env")

# class ResearchResponse(BaseModel):
#     topic: str
#     summary: str
#     sources: list[str]
#     tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=secrets["GOOGLE_API_KEY"])
#parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Research
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            "You are a research assistant that will help generate a research paper. "
            "FOR LATEST information use the tools at your disposal."
            "Provide three paragraphs of 5 lines/500 characters each."),
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
) 

tools = [search_tool, wiki_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("What information you want to research today? ")
raw_response = agent_executor.invoke({"query": query})
print(raw_response)

# Save to file
try:
    structured_response = raw_response.get("output")
    print("-------------------Structure response--------------------")
    
    print(structured_response)

    response = structured_response

    prompt_save = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a junior assistant that will help save research in a markdown format.
                You will receive research data and MUST call the appropriate tool to save it to a text file.
                File will start with Topic: add research topic here, then Summary: Add rest of the data
                DO NOT generate the output yourself. ONLY call the tool to save the data.
                """,
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{query}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )#.partial(format_instructions=parser.get_format_instructions())  # This is leading to Tool Call Mismanagement, LLM pretending to use tools.

    tools_save = [save_tool]
    agent_save = create_tool_calling_agent(
    llm=llm,
    prompt=prompt_save,
    tools=tools_save
    )

    save_executor = AgentExecutor(agent=agent_save, tools=tools_save, verbose=True)
    response = save_executor.invoke({"query": json.dumps(response, indent=2)})
    print("Save tool response:", response)


except Exception as e:
    print("Error parsing output, ", e, "Raw response - \n", raw_response)





