from transformers import pipeline

_generators = {}

SUPPORTED_MODELS = {
    "gpt2": "gpt2",
    "distilgpt2": "distilgpt2",
    "llama2-7b": "meta-llama/Llama-2-7b-hf",
    "llama2-13b": "meta-llama/Llama-2-13b-hf",
    "mistral-7b": "mistralai/Mistral-7B-v0.1",
    "gpt4all-vicuna": "nomic-ai/gpt4all-vicuna",
}


def get_generator(model_name: str):
    """Return a cached text-generation pipeline for a given model."""
    name = SUPPORTED_MODELS.get(model_name, model_name)
    if name not in _generators:
        _generators[name] = pipeline(
            "text-generation",
            model=name,
            device_map={"": -1},
            max_length=150,
            do_sample=True,
            temperature=0.7,
        )
    return _generators[name]
