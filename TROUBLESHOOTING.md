# Tavily MCP Server Troubleshooting

If you're experiencing issues with the Tavily MCP server in Claude, follow these steps:

## 1. Completely Restart Claude

1. Close Claude Desktop completely
2. Open Task Manager (Ctrl+Shift+Esc)
3. Find any Claude-related processes and end them
4. Restart Claude Desktop

## 2. Check Server Installation

1. Run the following command to verify the server is installed:
   ```
   uv run mcp install combined.py
   ```
2. You should see "Successfully installed TAVILY SEARCH in Claude app"

## 3. Common Issues and Solutions

### "No module named 'tavily'" Error

This error occurs when Claude can't find the Tavily Python package. Our `combined.py` script should handle this automatically by:
1. Checking if Tavily is installed
2. Installing it if not found
3. Using proper error reporting to stderr

### Error Logs Show No Output

If you're not seeing any error details, try running:
```
uv run mcp run combined.py
```

This will show detailed output that can help diagnose issues.

### API Key Issues

If you're getting authentication errors from Tavily, verify:
1. Your .env file contains a valid API key
2. The key is correctly formatted
3. The key has the necessary permissions

## 4. Still Having Issues?

1. Completely uninstall and reinstall the server:
   ```
   uv run mcp uninstall "TAVILY SEARCH"
   uv run mcp install combined.py
   ```
   
2. Check the Claude logs for more detailed error information 