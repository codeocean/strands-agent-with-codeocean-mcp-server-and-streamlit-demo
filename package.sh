#!/bin/bash

# Code Ocean MCP Agent - Package Generator
# This script creates a zip package of the project excluding .gitignore items

set -e  # Exit on any error

echo "🚀 Creating Code Ocean MCP Agent package..."

# Get the current directory name for the zip file
PROJECT_NAME=$(basename "$PWD")
ZIP_NAME="${PROJECT_NAME}-package.zip"

# Remove existing zip file if it exists
if [ -f "$ZIP_NAME" ]; then
    echo "📦 Removing existing package: $ZIP_NAME"
    rm "$ZIP_NAME"
fi

echo "📁 Including essential files:"
echo "  - code/ directory (Python source files)"
echo "  - README.md"
echo "  - pyproject.toml"
echo "  - uv.lock"
echo "  - .gitignore"

echo "🚫 Excluding:"
echo "  - __pycache__/ directories"
echo "  - .env files"
echo "  - scratch/ directory"
echo "  - .vscode/ directory"
echo "  - Virtual environments"
echo "  - Build artifacts"

# Create the zip file with specific inclusions and exclusions
zip -r "$ZIP_NAME" \
    code/ \
    README.md \
    pyproject.toml \
    uv.lock \
    .gitignore \
    -x \
    "*/__pycache__/*" \
    "*.pyc" \
    "*.pyo" \
    "build/*" \
    "dist/*" \
    "wheels/*" \
    "*.egg-info/*" \
    ".venv/*" \
    ".env" \
    "scratch/*" \
    ".vscode/*"

# Check if zip was created successfully
if [ -f "$ZIP_NAME" ]; then
    echo "✅ Package created successfully: $ZIP_NAME"
    echo "📊 Package size: $(du -h "$ZIP_NAME" | cut -f1)"
    echo "📋 Contents:"
    unzip -l "$ZIP_NAME" | head -20
    if [ $(unzip -l "$ZIP_NAME" | wc -l) -gt 25 ]; then
        echo "   ... and more files"
    fi
else
    echo "❌ Failed to create package"
    exit 1
fi

echo ""
echo "🎉 Package ready for distribution!"
echo "📤 You can now share: $ZIP_NAME"
