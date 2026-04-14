import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("KONTEXT_API_KEY", "")

if API_KEY:
    os.environ["KONTEXT_API_KEY"] = API_KEY

from kontext.server import mcp

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8000)
