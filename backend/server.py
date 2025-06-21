from fastapi import FastAPI, Request
from transformers import pipeline

generators = {}

def get_generator(model_name: str):
    """Return a cached text-generation pipeline for the given model."""
    if model_name not in generators:
        generators[model_name] = pipeline(
            'text-generation',
            model=model_name,
            device_map={'': -1},
            max_length=150,
            do_sample=True,
            temperature=0.7,
        )
    return generators[model_name]

app = FastAPI(title="ScamScanner Local API")

@app.post('/analyze')
async def analyze(req: Request):
    """
    Analizuje przekazany tekst i zwraca wygenerowaną odpowiedź z lokalnego modelu.
    Body JSON: { "text": "Twój tekst" }
    Odpowiedź JSON: { "result": "wygenerowany tekst" }
    """
    data = await req.json()
    text = data.get('text', '')
    model = data.get('model', 'gpt2')

    generator = get_generator(model)
    generated = generator(text, num_return_sequences=1)[0]['generated_text']
    return { 'result': generated }