import os
from typing import Optional

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

API_KEY = os.getenv("KONTEXT_API_KEY", "")

PORT = int(os.getenv("PORT", 8080))
HOST = os.getenv("HOST", "0.0.0.0")

mcp = FastMCP("kontext", host=HOST, port=PORT)


@mcp.tool()
def get_context(user_id: str) -> dict:
    """Retrieve context for a user."""
    from kontext.storage import load_context
    return load_context(user_id)


@mcp.tool()
def save_context_tool(user_id: str, context: dict) -> bool:
    """Save context for a user."""
    from kontext.storage import save_context
    return save_context(user_id, context)


@mcp.tool()
def list_contexts_tool() -> list[str]:
    """List all user IDs that have stored contexts."""
    from kontext.storage import list_contexts
    return list_contexts()


@mcp.tool()
def delete_context_tool(user_id: str) -> bool:
    """Delete context for a user."""
    from kontext.storage import delete_context
    return delete_context(user_id)


def validate_request(api_key: Optional[str]) -> bool:
    if not API_KEY:
        return True
    return api_key == API_KEY
