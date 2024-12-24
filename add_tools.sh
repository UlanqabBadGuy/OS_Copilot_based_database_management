#!/bin/bash

# Path to the tools directory
TOOLS_DIR="tools"

# Iterate over each .py file in the tools directory
for TOOL_PATH in "$TOOLS_DIR"/*.py; do
  # Check if there are any .py files
  if [ ! -f "$TOOL_PATH" ]; then
    echo "No .py files found in $TOOLS_DIR."
    exit 1
  fi
  
  # Extract the tool name from the file name
  TOOL_NAME=$(basename "$TOOL_PATH" .py)
  
  # Execute the command to add the tool
  python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name "$TOOL_NAME" --tool_path "$TOOL_PATH"
done