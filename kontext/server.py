import os
from typing import Optional

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

API_KEY = os.getenv("KONTEXT_API_KEY", "")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "contexts")


def get_storage_path(user_id: str) -> str:
    import json
    safe_user_id = user_id.replace("/", "_").replace("\\", "_")
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, f"{safe_user_id}.json")


def load_context(user_id: str) -> dict:
    import json
    path = get_storage_path(user_id)
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def save_context(user_id: str, context: dict) -> bool:
    import json
    path = get_storage_path(user_id)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(context, f, indent=2, ensure_ascii=False)
        return True
    except IOError:
        return False


def list_contexts() -> list[str]:
    os.makedirs(DATA_DIR, exist_ok=True)
    contexts = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            contexts.append(filename[:-5])
    return sorted(contexts)


def delete_context(user_id: str) -> bool:
    path = get_storage_path(user_id)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False


mcp = FastMCP("kontext")


@mcp.tool()
def get_context(user_id: str) -> dict:
    """Retrieve context for a user."""
    return load_context(user_id)


@mcp.tool()
def save_context_tool(user_id: str, context: dict) -> bool:
    """Save context for a user."""
    return save_context(user_id, context)


@mcp.tool()
def list_contexts_tool() -> list[str]:
    """List all user IDs that have stored contexts."""
    return list_contexts()


@mcp.tool()
def delete_context_tool(user_id: str) -> bool:
    """Delete context for a user."""
    return delete_context(user_id)


def validate_request(api_key: Optional[str]) -> bool:
    if not API_KEY:
        return True
    return api_key == API_KEY
