#!/bin/bash

# Define function to handle errors
handle_error() {
    echo "Error occurred: $1"
    exit 1
}

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

echo "Installing Python dependencies from requirements.txt..."
# Install Python dependencies
pip install -r "$DIR/requirements.txt" || handle_error "Failed to install Python dependencies"

echo "Applying database migrations..."
# Run database migration script
python3 manage.py migrate || handle_error "Database migration failed"

echo "Creating tables from fitness.sql..."
# Run fitness.sql to create required tables
mysql -h "localhost" -u "root" -p"raghvendra" "gymdb" < "$DIR/fitness.sql" || handle_error "Failed to execute fitness.sql"

echo "Collecting static files..."
# Collect static files
python3 manage.py collectstatic --noinput || handle_error "Failed to collect static files"

# Deactivate the virtual environment
deactivate

echo "Build completed successfully."
