from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str
    force_rag: bool = False

class AnalyzeResponse(BaseModel):
    result: str
    used_rag: bool