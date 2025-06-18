from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import openai
from transformers import pipeline
from config import settings
from cache import cache
from news_fetcher import fetch_latest_fragments
from models import AnalyzeRequest, AnalyzeResponse
from logger import logger

# Initialize OpenAI API
openai.api_key = settings.openai_api_key
app = FastAPI(title="ScamScanner API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

local_generator = pipeline(
    "text-generation",
    model=settings.local_model,
    device_map={"": -1},
    max_length=settings.summary_length,
    do_sample=True,
    temperature=0.7,
)

def call_local(prompt: str) -> str:
    logger.info("Using local model")
    out = local_generator(prompt, num_return_sequences=1)[0]["generated_text"]
    return out

def call_gpt4(prompt: str) -> str:
    logger.info("Using GPT-4 API")
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"system","content":"You are a fact-checker."},
                  {"role":"user","content":prompt}]
    )
    return resp.choices[0].message.content

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    key = hash(req.text + str(req.force_rag))
    if key in cache:
        logger.info("Cache hit")
        return AnalyzeResponse(result=cache[key])

    prompt = f"Analyse the following text for fake news:\n\n{req.text}"
    # Prosta heurystyka: jeśli wymuszone lub zawiera 'dziś', 'wczoraj'
    if req.force_rag or any(w in req.text.lower() for w in ["dziś","wczoraj","ostatnio"]):
        context = fetch_latest_fragments(req.text)
        prompt = f"Based on these fragments:\n{context}\n\nCheck: {req.text}"
        result = call_gpt4(prompt)
    else:
        result = call_local(prompt)

    cache[key] = result
    return AnalyzeResponse(result=result)
