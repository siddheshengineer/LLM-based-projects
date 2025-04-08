# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from core import run_research, save_research
from fastapi import HTTPException
import re


# Setup fastAPI app
app = FastAPI(
    title="Research Assistant API",
    description="An AI-powered research assistant that generates and saves research papers",
    version="1.0.0"
)

# Initialize Jinja templated
templates = Jinja2Templates(directory="./templates")

# Create directory and mount it
import os
os.makedirs("./downloads", exist_ok=True)
app.mount("/downloads", StaticFiles(directory="./downloads"), name="downloads")

# Render landing page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Render research page and call appropriate functions.
@app.post("/research", response_class=HTMLResponse)
async def research(request: Request, query: str = Form(...)):
    try:
        structure_response = run_research(query)
        save_response = save_research(structure_response)
        #print(save_response)
        match = re.search(r"(/downloads/[\w\-]+\.txt)", save_response)
        file_path = match.group(1) if match else None
        if file_path is None:
            match = re.search(r"(\/downloads\/.*?\.txt)", save_response)
            file_path = match.group(1) if match else None
        print(save_response, "\n", file_path)
        return templates.TemplateResponse("result.html", {"request": request, "query": query, "output": structure_response, "save_msg": file_path})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Research generation failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
