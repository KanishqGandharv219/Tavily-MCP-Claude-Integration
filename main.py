import sys
import os
import traceback

# Add the current directory to the path to ensure imports work
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from mcp.server.fastmcp import FastMCP
    from dotenv import load_dotenv
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize MCP server
    mcp = FastMCP("TAVILY SEARCH")
    
    # Get Tavily API key
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY not found in environment variables")
        sys.exit(1)
    
    try:
        # Import Tavily here to catch import errors
        from tavily import TavilyClient
        
        # Initialize Tavily client
        print(f"Initializing Tavily client with API key: {api_key[:4]}...{api_key[-4:]}")
        tavily = TavilyClient(api_key=api_key)
        
        @mcp.tool()
        def search(query: str, search_depth: str = "basic") -> dict:
            """
            Perform a web search using Tavily
            
            Args:
                query: The search query to execute
                search_depth: Either 'basic' or 'deep' search
            """
            print(f"Searching for: {query} (depth: {search_depth})")
            response = tavily.search(
                query=query,
                search_depth=search_depth
            )
            return response
        
        @mcp.tool()
        def analyze_text(text: str) -> dict:
            """
            Analyze text using Tavily's text analysis capability
            
            Args:
                text: The text content to analyze
            """
            print(f"Analyzing text: {text[:50]}...")
            response = tavily.analyze_text(text=text)
            return response
        
        if __name__ == "__main__":
            print("Starting Tavily MCP server. Waiting for Claude requests...")
            mcp.run()
            
    except ImportError as e:
        print(f"ERROR: Could not import tavily module: {e}")
        print("Please make sure the tavily-python package is installed.")
        print("Try: pip install tavily-python")
        sys.exit(1)
except Exception as e:
    print(f"ERROR: {e}")
    traceback.print_exc()
    sys.exit(1)
