from setuptools import setup, find_packages

setup(
    name="tavily-mcp",
    version="0.1.0",
    description="Tavily MCP server for Claude",
    packages=find_packages(),
    install_requires=[
        "mcp[cli]>=1.6.0",
        "tavily-python",
        "python-dotenv",
    ],
    python_requires=">=3.10",
) 