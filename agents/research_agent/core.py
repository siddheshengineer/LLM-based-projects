from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
from dotenv import dotenv_values


secrets = dotenv_values(".env")
google_api_key=secrets["GOOGLE_API_KEY"]
if not google_api_key:
    raise  ValueError("API key missing")

# Initialize LLM model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key)


# ----------------- Research Agent Setup -----------------
# Define the prompt for generating research
research_prompt = ChatPromptTemplate.from_messages(
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

research_tools = [search_tool, wiki_tool]
research_agent = create_tool_calling_agent(
    llm=llm,
    prompt=research_prompt,
    tools=research_tools
)
research_executor = AgentExecutor(agent=research_agent, tools=research_tools, verbose=True)



# ----------------- Save Agent Setup -----------------
# Define the prompt for saving research data in markdown format
save_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    You are a junior assistant that will help save research in a markdown format.
                    You will receive research data and MUST call the appropriate tool to save it to a text file.
                    File will start with Topic: add research topic here, then Summary: Add rest of the data
                    DO NOT generate the output yourself. ONLY call the tool to save the data.
                    AFTER SAVING, you MUST return a response in EXACTLY the following format on a single line:
            
                    File    Path: /downloads/<your_saved_filename.txt>
                    
                    DO NOT include any additional text.
                    """,
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{query}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

save_tools = [save_tool]
save_agent = create_tool_calling_agent(
    llm=llm,
    prompt=save_prompt,
    tools=save_tools
    )
save_executor = AgentExecutor(agent=save_agent, tools=save_tools, verbose=True)

def run_research(query: str) -> str: # Run the research and returns response
    result = research_executor.invoke({"query": query})
    return result.get("output")

def save_research(data: str) -> str:  # Saves research data to a file
    response = save_executor.invoke({"query": data})
    return response.get("output")
