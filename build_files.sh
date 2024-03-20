#!/bin/bash

# Define function to handle errors
handle_error() {
    echo "Error occurred: $1"
    exit 1
}

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip || handle_error "Failed to upgrade pip"

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew is not installed. Please install Homebrew and try again."
    handle_error "Homebrew not found"
fi

# Install MySQL client dependencies
echo "Installing MySQL client dependencies..."
brew install mysql || handle_error "Failed to install MySQL client dependencies"

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Activate the virtual environment
source "$DIR/myenv/bin/activate" || handle_error "Failed to activate virtual environment"

# Check if dotenv is installed
if ! python3 -c "import dotenv" &> /dev/null; then
    echo "dotenv is not installed. Installing dotenv..."
    pip install python-dotenv || handle_error "Failed to install dotenv"
fi

# Check if Django is installed
if ! python3 -c "import django" &> /dev/null; then
    echo "Django is not installed. Installing Django..."
    pip install django || handle_error "Failed to install Django"
fi

echo "Installing system dependencies for MySQL client..."
# Install MySQL client library using pip
pip install mysqlclient || handle_error "Failed to install system dependencies for MySQL client"

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt...
