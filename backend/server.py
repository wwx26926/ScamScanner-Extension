from import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

generator = pipeline("text-generation", model="distilgpt2", device_map={"": -1}, max_length=512, do_sample=True, temperature=0.7)

@app.post("/analyze")
async def analyze_text(req: Request):
    data = await req.json()
    prompt = (
        "Oceń, czy poniższy tekst zawiera nieprawdziwe informacje.\n\n"
        f"---\n{data.get('text','')}\n---\nOdpowiedź:"
    )
    out = generator(prompt, max_new_tokens=256, num_return_sequences=1)[0]["generated_text"]
    return {"result": out.replace(prompt, "").strip()}
