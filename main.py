from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from groq import Groq
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

app.add_middleware(CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

groq_client = Groq(api_key=GROQ_API_KEY)

class LoveLetterRequest(BaseModel):
    sender_name: str
    receiver_name: str
    additional_info: Optional[str] = None

class PoemRequest(BaseModel):
    requests: Optional[str]


@app.get("/")
def index_route():
    return {"hello":"world"}


@app.post("/generate-love-letter")
async def generate_love_letter(request: LoveLetterRequest):
    try:
        prompt = f"""
    Write a heartfelt love letter from {request.sender_name} to {request.receiver_name}.
    Incorporate the following additional information: {request.additional_info}.
    Make the letter personal, unique, natural-sounding and avoid generic phrases.
    The letter should be sincere and express deep affection and appreciation.
    Keep the length between 150 and 200 words.
    Separate each line using newline characters.
        """
        chat_completion= groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=1,
        )
        
        love_letter = chat_completion.choices[0].message.content
        prefix = f"Here is a heartfelt love letter from {request.sender_name} to {request.receiver_name}:\n\n"
        love_letter = love_letter.removeprefix(prefix)
        love_letter = love_letter.splitlines()
        
        return {"love_letter" : love_letter}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        return {"error": str(e)}
        

