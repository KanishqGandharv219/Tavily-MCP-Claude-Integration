#!/usr/bin/env python
import sys
import os

# Setup error reporting to stderr
def debug_print(msg):
    print(msg, file=sys.stderr)

debug_print("Starting Tavily MCP initialization...")

# Try installing tavily if it's not found
try:
    debug_print("Checking for tavily-python...")
    import tavily
    debug_print(f"Found tavily module at: {tavily.__file__}")
except ImportError:
    debug_print("tavily-python not found, attempting to install it...")
    try:
        import subprocess
        debug_print(f"Using Python executable: {sys.executable}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tavily-python", "python-dotenv"])
        debug_print("Installation successful!")
        try:
            import tavily
            debug_print(f"Successfully imported tavily from: {tavily.__file__}")
        except ImportError as e:
            debug_print(f"Failed to import tavily after installation: {e}")
            sys.exit(1)
    except Exception as e:
        debug_print(f"Failed to install tavily-python: {e}")
        sys.exit(1)

# Now try importing required modules
try:
    debug_print("Importing required modules...")
    from mcp.server.fastmcp import FastMCP
    import os
    from dotenv import load_dotenv
    from tavily import TavilyClient
    
    # Load environment variables from .env file if available
    if os.path.exists(".env"):
        debug_print("Loading .env file...")
        load_dotenv()
    else:
        debug_print("No .env file found, using environment variables directly")
    
    # Initialize MCP server
    debug_print("Initializing MCP server...")
    mcp = FastMCP("TAVILY SEARCH")
    
    # Get Tavily API key
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        debug_print("ERROR: TAVILY_API_KEY not found in environment variables")
        # Fallback to hardcoded key for demonstration
        api_key = "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"
        debug_print("Using fallback API key")
    
    # Initialize Tavily client
    debug_print(f"Initializing Tavily client with API key: {api_key[:4]}...{api_key[-4:]}")
    tavily = TavilyClient(api_key=api_key)
    
    @mcp.tool()
    def search(query: str, search_depth: str = "basic") -> dict:
        """
        Perform a web search using Tavily
        
        Args:
            query: The search query to execute
            search_depth: Either 'basic' or 'deep' search
        """
        debug_print(f"Searching for: {query} (depth: {search_depth})")
        try:
            response = tavily.search(
                query=query,
                search_depth=search_depth
            )
            debug_print("Search completed successfully")
            return response
        except Exception as e:
            debug_print(f"Error in search: {e}")
            return {"error": str(e)}
    
    @mcp.tool()
    def analyze_text(text: str) -> dict:
        """
        Analyze text using Tavily's text analysis capability
        
        Args:
            text: The text content to analyze
        """
        debug_print(f"Analyzing text: {text[:50]}...")
        try:
            response = tavily.analyze_text(text=text)
            debug_print("Text analysis completed successfully")
            return response
        except Exception as e:
            debug_print(f"Error in analyze_text: {e}")
            return {"error": str(e)}
    
    debug_print("All tools registered, starting server...")
    
    # Start the server
    if __name__ == "__main__":
        debug_print("Starting Tavily MCP server. Waiting for Claude requests...")
        mcp.run()
    
except Exception as e:
    debug_print(f"ERROR in setup: {e}")
    import traceback
    debug_print(traceback.format_exc())
    sys.exit(1) 