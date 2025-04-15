from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crawler import scrape_all_text
from llm_runner import ask_llm
import traceback

app = FastAPI()

class ExtractRequest(BaseModel):
    url: str

@app.post("/extract-data/")
def extract_data(req: ExtractRequest):
    try:
        # Step 1: Scrape all visible text from the website
        website_text = scrape_all_text(req.url)
        if not website_text.strip():
            raise ValueError("No readable text was extracted from the given URL.")

        # Step 2: Ask LLM to process and extract useful data
        prompt = f"Extract structured and useful data from the following website content:\n\n{website_text}\n\nAnswer:"
        answer = ask_llm(prompt)

        return {"extracted_data": answer.strip()}

    except Exception as e:
        traceback.print_exc()  # This will print the full error in terminal
        raise HTTPException(status_code=500, detail=str(e))
