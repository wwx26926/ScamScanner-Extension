
try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    import faiss
except Exception:  # pragma: no cover - optional deps
    SentenceTransformer = None  # type: ignore
    faiss = None  # type: ignore
    np = None  # type: ignore

class EmbeddingStore:
    """Simple FAISS-backed vector store with a graceful fallback."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.texts: list[str] = []
        if SentenceTransformer is None or faiss is None or np is None:
            self.model = None
            self.index = None
        else:
            self.model = SentenceTransformer(model_name)
            dim = self.model.get_sentence_embedding_dimension()
            self.index = faiss.IndexFlatL2(dim)

    def add(self, text: str) -> None:
        self.texts.append(text)
        if self.model is not None and self.index is not None:
            emb = self.model.encode([text])[0]
            self.index.add(np.array([emb]).astype("float32"))

    def search(self, query: str, k: int = 3) -> list[str]:
        if not self.texts:
            return []
        if self.model is None or self.index is None or np is None:
            matches = [t for t in self.texts if query.lower() in t.lower()]
            if len(matches) < k:
                matches += self.texts[:k]
            return matches[:k]
        emb = self.model.encode([query])[0]
        dists, idxs = self.index.search(np.array([emb]).astype("float32"), k)
        return [self.texts[i] for i in idxs[0] if i < len(self.texts)]

vector_store = EmbeddingStore()
