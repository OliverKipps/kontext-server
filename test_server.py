from kontext.server import mcp

print("Server imports OK")
print("Settings:", mcp.settings)
print("Host:", getattr(mcp.settings, 'host', 'N/A'))
print("Port:", getattr(mcp.settings, 'port', 'N/A'))
