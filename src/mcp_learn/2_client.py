from mcp.server.fastmcp import FastMCP
from mcp.client.stdio import stdio_client
from mcp import ClientSession,types,StdioServerParameters


server_parameters = StdioServerParameters(
    command = "mcp",
    args = ["run","server.py"],
    env = None
)


