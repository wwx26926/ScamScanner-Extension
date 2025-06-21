wl279k-codex/wyświetl-wynik-analizy-w-oknie-przeglądarki
from collections import Counter
from typing import List


def _embed(text: str) -> Counter:
    return Counter(text.lower().split())


class EmbeddingStore:
    """Simple in-memory store using bag-of-words Jaccard similarity."""

    def __init__(self):
        self.texts: List[str] = []
        self.vectors: List[Counter] = []

    def add(self, text: str) -> None:
        self.texts.append(text)
        self.vectors.append(_embed(text))

    def search(self, query: str, k: int = 3) -> List[str]:
        if not self.texts:
            return []
        q = _embed(query)

        def score(v: Counter) -> float:
            inter = sum((q & v).values())
            union = sum((q | v).values())
            return inter / union if union else 0.0

        ranked = sorted(range(len(self.vectors)), key=lambda i: score(self.vectors[i]), reverse=True)
        return [self.texts[i] for i in ranked[:k]]

from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class EmbeddingStore:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        dim = self.model.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatL2(dim)
        self.texts: list[str] = []

    def add(self, text: str) -> None:
        emb = self.model.encode([text])[0]
        self.index.add(np.array([emb]).astype("float32"))
        self.texts.append(text)

    def search(self, query: str, k: int = 3) -> list[str]:
        if not self.texts:
            return []
        emb = self.model.encode([query])[0]
        dists, idxs = self.index.search(np.array([emb]).astype("float32"), k)
        return [self.texts[i] for i in idxs[0] if i < len(self.texts)]

vector_store = EmbeddingStore()
