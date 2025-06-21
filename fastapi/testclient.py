import asyncio
from typing import Any
from . import Request, Response, FastAPI

class TestClient:
    def __init__(self, app: FastAPI):
        self.app = app

    def post(self, path: str, json: dict | None = None) -> Response:
        handler = self.app.routes.get(("POST", path))
        if handler is None:
            return Response({"detail": "Not Found"}, status_code=404)
        req = Request(json or {})
        if asyncio.iscoroutinefunction(handler):
            data = asyncio.get_event_loop().run_until_complete(handler(req))
        else:
            data = handler(req)
        return Response(data, status_code=200)
