import os
from functools import wraps
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("KONTEXT_API_KEY", "")


def get_api_key() -> Optional[str]:
    return API_KEY if API_KEY else None


def validate_api_key(request_api_key: Optional[str]) -> bool:
    if not API_KEY:
        return True
    if not request_api_key:
        return False
    return request_api_key == API_KEY


def require_auth(func):
    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("x-api-key", "")
        if not validate_api_key(auth_header):
            from starlette.responses import JSONResponse
            return JSONResponse(
                status_code=401,
                content={"error": "Unauthorized", "message": "Invalid or missing API key"}
            )
        return await func(request, *args, **kwargs)
    return wrapper
