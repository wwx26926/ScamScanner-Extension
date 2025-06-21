class SentenceTransformer:
    def __init__(self, model_name: str = "stub"):
        self.model_name = model_name

    def encode(self, texts):
        # simple embedding: word length vector
        return [[len(t)] for t in texts]

    def get_sentence_embedding_dimension(self):
        return 1
