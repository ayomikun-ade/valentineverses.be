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
model = "llama-3.3-70b-versatile"

class LoveLetterRequest(BaseModel):
    sender_name: str
    receiver_name: str
    additional_info: Optional[str] = None

class PoemRequest(BaseModel):
    requests: Optional[str] = None 


@app.get("/")
def index_route():
    return {"hello":"world"}


@app.post("/generate-love-letter")
async def generate_love_letter(request: LoveLetterRequest):
    try:
        prompt = f"""
    Write a heartfelt, personalized love letter from {request.sender_name} to {request.receiver_name}.
    Incorporate the following additional information naturally and creatively: {request.additional_info}.
    Make the letter completely unique, natural-sounding, and avoid generic phrases or clichés like "I love you more than words can say" or "You are my everything."
    Express deep affection, appreciation, and specific memories, qualities, or shared experiences that make the relationship special.
    Structure the letter with a warm, personalized greeting, 2-3 paragraphs of heartfelt content, and a sincere, unique closing.
    Keep the total length between 150-200 words.
    Use vivid, emotional language, varied sentence structures, and creative metaphors to make it engaging and memorable.
    Separate each line using newline characters for proper formatting.
        """
        chat_completion= groq_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=1,
        )
        
        love_letter = chat_completion.choices[0].message.content
        
        return {"love_letter" : love_letter}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        # return {"error": str(e)}
        
@app.post("/generate-poem")
async def generate_pem(request: PoemRequest):
    prompt = f"""
    Write a beautiful, romantic poem inspired by love and passion.
    Consider these specific requests: {request.requests}.
    The poem should evoke strong emotions, vivid imagery, and a sense of deep connection.
    Choose a style that fits the requests—such as free verse, rhyming couplets, or sonnet form—but keep it accessible and heartfelt.
    Focus on themes like eternal love, shared moments, or the beauty of the beloved.
    Keep the poem concise: aim for 12-20 lines or 80-150 words total.
    Respond with only the contents of the poem, no titles or explanations.
    Separate each line using newline characters for proper poetic formatting.
    """
    try:
        chat_completion = groq_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=1,
        )
        
        poem = chat_completion.choices[0].message.content.splitlines()
        return {"poem": poem}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        # return {"error": str(e)}