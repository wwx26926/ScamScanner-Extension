import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))
from fastapi.testclient import TestClient
from backend.server import app, vector_store

client = TestClient(app)

def test_ingest_and_analyze():
    resp = client.post('/ingest', json={'texts': ['Paris is in France.']})
    assert resp.status_code == 200
    assert resp.json()['ingested'] == 1

    r = client.post('/analyze', json={'text': 'Where is Paris?', 'model': 'distilgpt2'})
    assert r.status_code == 200
    data = r.json()
    assert 'result' in data
