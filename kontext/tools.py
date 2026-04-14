from mcp.server.fastmcp import FastMCP

from kontext.storage import load_context, save_context, list_contexts, delete_context

mcp = FastMCP("kontext")


@mcp.tool()
def get_context(user_id: str) -> dict:
    """Retrieve context for a user.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        The stored context dictionary, or empty dict if none exists.
    """
    return load_context(user_id)


@mcp.tool()
def save_context_tool(user_id: str, context: dict) -> bool:
    """Save context for a user.
    
    Args:
        user_id: The unique identifier for the user.
        context: The context dictionary to store.
        
    Returns:
        True if successful, False otherwise.
    """
    return save_context(user_id, context)


@mcp.tool()
def list_contexts_tool() -> list[str]:
    """List all user IDs that have stored contexts.
    
    Returns:
        A list of user IDs with stored contexts.
    """
    return list_contexts()


@mcp.tool()
def delete_context_tool(user_id: str) -> bool:
    """Delete context for a user.
    
    Args:
        user_id: The unique identifier for the user.
        
    Returns:
        True if deleted, False if not found.
    """
    return delete_context(user_id)
