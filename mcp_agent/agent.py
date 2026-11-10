
from pathlib import Path

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StdioConnectionParams,
)
from mcp import StdioServerParameters


# 1. Create the filesystem directory
folder = Path(__file__).parent.joinpath("files").resolve()
folder.mkdir(parents=True, exist_ok=True)


# 2. Configure the MCP Filesystem Server
filesystem_toolset = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                str(folder),
            ],
        ),
    ),
)


# 3. Create the AI Agent
root_agent = Agent(
    model="gemini-3.5-flash",
    name="filesystem_agent",
    description="An AI assistant that manages files and folders.",
    instruction=f"""
    You are an intelligent filesystem assistant.

    Your job is to help users manage files and folders.

    Allowed directory:
    {folder}

    Instructions:
    1. Use MCP filesystem tools to perform file operations.
    2. Always use absolute paths.
    3. You can create, read, write, move, rename,
       and delete files when requested.
    4. List directory contents when requested.
    5. Never access files outside the allowed directory.
    6. Explain the result of every operation clearly.
    7. Ask for confirmation before destructive operations.
    """,
    tools=[filesystem_toolset],
)
