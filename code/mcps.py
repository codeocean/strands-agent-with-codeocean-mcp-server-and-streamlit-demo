
# code/mcps.py

# Initialize the MCP client for CodeOcean
# This client connects to the CodeOcean MCP server using the provided command and environment variables.
# required: uvx, mcp, strands.tools.mcp, environment variables CODEOCEAN_DOMAIN and CODEOCEAN_TOKEN

from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters
from contextlib import ExitStack
import os

stack = ExitStack()
codeocean_mcp = stack.enter_context(
    MCPClient(
        lambda: stdio_client(
            StdioServerParameters(command="uvx", args=["codeocean-mcp-server"], env={
                "CODEOCEAN_DOMAIN": os.environ.get("CODEOCEAN_DOMAIN", ""),
                "CODEOCEAN_TOKEN": os.environ.get("CODEOCEAN_TOKEN", "")
            })
        )
    ) # type: ignore
)

codeocean_tools = codeocean_mcp.list_tools_sync()
