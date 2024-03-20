#!/bin/bash

# Define function to handle errors
handle_error() {
    echo "Error occurred: $1"
    exit 1
}

# Activate the virtual environment
source /Users/clanap.technologies/Downloads/gymTest/myenv/bin/activate || handle_error "Failed to activate virtual environment"

# Check if dotenv is installed
if ! python -c "import dotenv" &> /dev/null; then
    echo "dotenv is not installed. Installing dotenv..."
    pip install python-dotenv || handle_error "Failed to install dotenv"
fi

# Check if Django is installed
if ! python -c "import django" &> /dev/null; then
    echo "Django is not installed. Installing Django..."
    pip install django || handle_error "Failed to install Django"
fi

echo "Installing system dependencies for MySQL client..."
# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew is not installed. Please install Homebrew and try again."
    handle_error "Homebrew not found"
fi

# Install MySQL client library
brew install libmysqlclient-dev || handle_error "Failed to install system dependencies for MySQL client"

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt || handle_error "Failed to install Python dependencies"

# Run database migration script
echo "Applying database migrations..."
python manage.py migrate || handle_error "Database migration failed"

# Run fitness.sql to create required tables
echo "Creating tables from fitness.sql..."
mysql -h "localhost" -u "root" -p"raghvendra" "gymdb" < fitness.sql || handle_error "Failed to execute fitness.sql"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput || handle_error "Failed to collect static files"

# Deactivate the virtual environment
deactivate

echo "Build completed successfully."
