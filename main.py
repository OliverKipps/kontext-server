import os

API_KEY = os.getenv("KONTEXT_API_KEY", "")

PORT = int(os.getenv("PORT", 8080))
HOST = os.getenv("HOST", "0.0.0.0")

print(f"Starting KONTEXT server on {HOST}:{PORT}", flush=True)

from mcp.server.fastmcp import FastMCP

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


if __name__ == "__main__":
    mcp.run(transport="streamable-http")