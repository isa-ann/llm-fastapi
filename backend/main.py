from fastapi import FastAPI, HTTPException, Query,Form
from pydantic import BaseModel
import os
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/get_gemini_completion")
async def get_gemini_completion(
                            gemini_api_key: str =Form(...),
                            prompt: str = Form(...),  
                        ):
    try:
        genai.configure(api_key = gemini_api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                stop_sequences=['space'],
                max_output_tokens=400,
                temperature=0)
        )
        print(response)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


