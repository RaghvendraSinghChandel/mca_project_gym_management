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

echo "Installing system dependencies for MySQL client..."
# Install MySQL client library using pip
pip install mysqlclient || handle_error "Failed to install system dependencies for MySQL client"

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
pip install -r "$DIR/requirements.txt" || handle_error "Failed to install Python dependencies"

# Run database migration script
echo "Applying database migrations..."
python3 manage.py migrate || handle_error "Database migration failed"

# Run fitness.sql to create required tables
echo "Creating tables from fitness.sql..."
mysql -h "localhost" -u "root" -p"raghvendra" "gymdb" < "$DIR/fitness.sql" || handle_error "Failed to execute fitness.sql"

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput || handle_error "Failed to collect static files"

# Deactivate the virtual environment
deactivate

echo "Build completed successfully."
