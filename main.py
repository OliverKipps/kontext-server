from dotenv import load_dotenv

load_dotenv()

from kontext.server import mcp

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
