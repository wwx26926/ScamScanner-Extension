import asyncio
from typing import Callable, Awaitable, Dict, Any, Tuple

class Request:
    def __init__(self, data: Dict[str, Any]):
        self._data = data or {}

    async def json(self) -> Dict[str, Any]:
        return self._data

class FastAPI:
    def __init__(self, title: str | None = None):
        self.routes: Dict[Tuple[str, str], Callable] = {}

    def post(self, path: str):
        def decorator(func: Callable[[Request], Awaitable[Any]] | Callable[[Request], Any]):
            self.routes[("POST", path)] = func
            return func
        return decorator

# simple response wrapper used in tests
class Response:
    def __init__(self, data: Any, status_code: int = 200):
        self._data = data
        self.status_code = status_code

    def json(self) -> Any:
        return self._data

