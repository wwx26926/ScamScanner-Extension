from fastapi import FastAPI, Request
from model_factory import get_generator
from embedding import vector_store
from planner import start as start_planner

app = FastAPI(title="ScamScanner Local API")

# start background update tasks
start_planner()

@app.post('/ingest')
async def ingest(req: Request):
    data = await req.json()
    texts = data.get('texts', [])
    for t in texts:
        vector_store.add(t)
    return {'ingested': len(texts)}

@app.post('/search')
async def search(req: Request):
    data = await req.json()
    query = data.get('query', '')
    results = vector_store.search(query)
    return {'results': results}

@app.post('/analyze')
async def analyze(req: Request):
    data = await req.json()
    text = data.get('text', '')
    model = data.get('model', 'gpt2')
    fact_check = data.get('fact_check', False)

    context = "\n".join(vector_store.search(text))
    prompt = f"{context}\n\n{text}" if context else text

    generator = get_generator(model)
    generated = generator(prompt, num_return_sequences=1)[0]['generated_text']

    verified = True
    if fact_check:
        verified = 'uncertain' not in generated.lower()

    return {'result': generated, 'fact_check': verified}
