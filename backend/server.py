from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI(title="ScamScanner Local API")

# Inicjalizacja lokalnego modelu (np. gpt2 lub inny dostępny)
local_generator = pipeline(
    'text-generation',
    model='gpt2',           # zmień na swoją ścieżkę lub nazwę modelu
    device_map={'': -1},    # CPU
    max_length=150,
    do_sample=True,
    temperature=0.7,
)

@app.post('/analyze')
async def analyze(req: Request):
    """
    Analizuje przekazany tekst i zwraca wygenerowaną odpowiedź z lokalnego modelu.
    Body JSON: { "text": "Twój tekst" }
    Odpowiedź JSON: { "result": "wygenerowany tekst" }
    """
    data = await req.json()
    text = data.get('text', '')

    # Generujemy odpowiedź lokalnie
    generated = local_generator(text, num_return_sequences=1)[0]['generated_text']
    return { 'result': generated }