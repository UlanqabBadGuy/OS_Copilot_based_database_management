#!/bin/bash

# Path to the tools directory
TOOLS_DIR="oscopilot/tool_repository/generated_tools/tool_code"

# Iterate over each .py file in the tools directory
for TOOL_PATH in "$TOOLS_DIR"/*.py; do
  # Skip __init__.py
  if [[ "$(basename "$TOOL_PATH")" == "__init__.py" ]]; then
    continue
  fi

  # Check if there are any .py files
  if [ ! -f "$TOOL_PATH" ]; then
    echo "No .py files found in $TOOLS_DIR."
    exit 1
  fi
  
  # Extract the tool name from the file name
  TOOL_NAME=$(basename "$TOOL_PATH" .py)
  
  # Execute the command to delete the tool
  echo "Deleting tool: $TOOL_NAME"
  python oscopilot/tool_repository/manager/tool_manager.py --delete --tool_name "$TOOL_NAME"
done
