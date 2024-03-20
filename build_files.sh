#!/bin/bash

# Define function to handle errors
handle_error() {
    echo "Error occurred: $1"
    exit 1
}

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip || handle_error "Failed to upgrade pip"

# Check if Django is installed
if ! python3 -c "import django" &> /dev/null; then
    echo "Django is not installed. Installing Django..."
    pip install django || handle_error "Failed to install Django"
fi

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Activate the virtual environment
source "$DIR/myenv/bin/activate" || handle_error "Failed to activate virtual environment"

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt || handle_error "Failed to install Python dependencies"


echo "Setup complete!"
