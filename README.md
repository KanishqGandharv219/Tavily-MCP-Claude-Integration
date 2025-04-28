# Tavily MCP Server for Claude

This project creates a Tavily search integration for Claude using the Model Completion Protocol (MCP).

## Setup Instructions

1. Clone this repository
2. Create a `.env` file in the root directory with your Tavily API key:
   ```
   TAVILY_API_KEY=your_tavily_api_key_here
   ```
   You can get your API key from [Tavily](https://tavily.com)
3. Install dependencies with `uv add "mcp[cli]" "tavily-python" "python-dotenv"`
4. Install the MCP server with `uv run mcp install main.py`

## Setup Steps (Already Completed)

1. Installed uv by running `pip install uv`
2. Created project directory with `uv init tavily-mcp-server`
3. Added MCP CLI with `uv add "mcp[cli]"`
4. Added required dependencies with `uv add "tavily-python" "python-dotenv"`
5. Upgraded typer library with `pip install --upgrade typer`
6. Created Tavily search server in `main.py`
7. Installed server in Claude with `uv run mcp install main.py`

## Using Tavily Search in Claude

1. Make sure Claude Desktop is restarted (close it completely from Task Manager first, then restart)
2. In Claude, you should see the Tavily Search tools available
3. You can ask Claude to search for information, for example:
   - "Search for the latest news about artificial intelligence"
   - "Find information about climate change"
   - "Look up the recipe for chocolate chip cookies"

## Available Tools

This server provides Claude with two Tavily-powered tools:

1. `search(query, search_depth)` - Performs web searches
2. `analyze_text(text)` - Analyzes text content

## Troubleshooting

If the tools don't appear in Claude:
1. Make sure you've restarted Claude completely
2. Try reinstalling the MCP server with `uv run mcp install main.py`
3. Check for any error messages during installation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
