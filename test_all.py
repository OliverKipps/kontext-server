print("Testing storage imports...")
from kontext.storage import load_context, save_context, delete_context, list_contexts
print("Storage imports OK")

print("Testing save/load...")
save_context('test', {'hello': 'world'})
result = load_context('test')
print("Save/Load result:", result)
delete_context('test')
print("Delete result:", load_context('test'))

print("Testing server import...")
from kontext.server import mcp
print("Server import OK")
print("Server settings host:", mcp.settings.host)
print("Server settings port:", mcp.settings.port)

print("All tests passed!")
