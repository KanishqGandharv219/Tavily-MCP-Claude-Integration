#!/usr/bin/env python
import sys
import os
import subprocess

# Get the directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the current directory to the path
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Print debugging information
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Current directory: {current_dir}")
print(f"PATH: {os.environ.get('PATH')}")
print(f"PYTHONPATH: {os.environ.get('PYTHONPATH')}")
print(f"Sys.path: {sys.path}")

# Try to import tavily to check if it's available
try:
    import tavily
    print(f"Tavily module found at: {tavily.__file__}")
except ImportError as e:
    print(f"ERROR: Could not import tavily: {e}")
    print("Installing tavily-python...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tavily-python", "python-dotenv"])
        print("Installation successful!")
    except Exception as e:
        print(f"Failed to install: {e}")

# Run the main script
try:
    print("Running main.py...")
    from main import mcp
    print("Starting Tavily MCP server...")
    mcp.run()
except Exception as e:
    print(f"Error running main.py: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1) 