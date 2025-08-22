from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import traceback
import tempfile
import os

from nepex_agent import generate_output, extract_use_case_context

# Load environment variables
load_dotenv()

# App and config setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Path to markdown file
MARKDOWN_FILE_PATH = "Nepex_Agent_Guide.md"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})


@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, use_case: str = Form(...), prompt: str = Form(...), context: str = Form("")):
    try:
        if not prompt.strip():
            return templates.TemplateResponse("index.html", {
                "request": request,
                "response": "Prompt input is required.",
                "prompt": prompt,
                "use_case": use_case,
                "context": context
            })

        # Load markdown guidance section for use_case
        md_context = extract_use_case_context(use_case, MARKDOWN_FILE_PATH)            
        output = await generate_output(
            prompt=prompt,
            use_case=use_case,
            context=context,
            md_context=md_context
        )

        return templates.TemplateResponse("index.html", {
            "request": request,
            "response": output,
            "prompt": prompt,
            "use_case": use_case,
            "context": context
        })

    except Exception as e:
        print("Error during /generate")
        traceback.print_exc()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "response": f"Error generating response: {str(e)}",
            "prompt": prompt,
            "use_case": use_case,
            "context": context
        })

@app.post("/export")
async def export(text: str = Form(...), use_case: str = Form(...)):
    try:
        filename = f"{use_case.lower().replace(' ', '_')}_nepex.txt"
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as tmp:
            tmp.write(text)
            tmp_path = tmp.name
        return FileResponse(tmp_path, filename=filename, media_type="text/plain")
    except Exception as e:
        return {"error": str(e)}