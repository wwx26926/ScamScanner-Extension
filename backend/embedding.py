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


vector_store = EmbeddingStore()
