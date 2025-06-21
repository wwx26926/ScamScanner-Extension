class DummyPipeline:
    def __call__(self, prompt: str, num_return_sequences: int = 1):
        return [{"generated_text": "stub response to: " + prompt}]

def pipeline(task: str, model: str | None = None, device_map=None, max_length=50, do_sample=False, temperature=1.0):
    return DummyPipeline()
