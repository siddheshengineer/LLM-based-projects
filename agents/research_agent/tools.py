from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = None):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if not filename:
        filename = f"research_{timestamp}.txt"
    
    # Ensure the downloads directory exists
    import os
    os.makedirs("./downloads", exist_ok=True)
    
    path = f"./downloads/{filename}"  # Save in static folder
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(path, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"/downloads/{filename}" 

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
