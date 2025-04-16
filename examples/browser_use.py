"""
Basic usage example for mcp_use.

This example demonstrates how to use the mcp_use library with MCPClient
to connect any LLM to MCP tools through a unified interface.

Special thanks to https://github.com/microsoft/playwright-mcp for the server.
"""

import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from mcp_use import MCPAgent, MCPClient
from mcp_use.logging import Logger


async def main():
    """Run the example using a configuration file."""
    # Load environment variables
    load_dotenv()

    # Configure logging
    Logger.configure(
        level="DEBUG",
        log_to_console=True,
        log_to_file="mcp_use.log"
    )

    # Create MCPClient from config file
    client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "browser_mcp.json"))

    # Create LLM
    llm = ChatOpenAI(model="o4-mini")
    # llm = ChatOpenAI(model="o3-mini")
    # llm = ChatOpenAI(model="gpt-4o")
    # llm = init_chat_model(model="llama-3.1-8b-instant", model_provider="groq")
    # llm = ChatAnthropic(model="claude-3-")
    # llm = ChatGroq(model="llama3-8b-8192")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Find the best restaurant in Hermosa Beach USING GOOGLE SEARCH",
        max_steps=30,
    )
    print(f"\nResult: {result}")


if __name__ == "__main__":
    # Run the appropriate example
    asyncio.run(main())
