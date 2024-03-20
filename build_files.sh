#!/bin/bash

# Define function to handle errors
handle_error() {
    echo "Error occurred: $1"
    exit 1
}

# # Check if environment variables are set
# if [[ -z "$DB_HOST" || -z "$DB_USER" || -z "$DB_PASSWORD" || -z "$DB_NAME" ]]; then
#     handle_error "One or more required environment variables are not set"
# fi

# Run database migration script
echo "Applying database migrations..."
python3.9 manage.py migrate || handle_error "Database migration failed"

# Run fitness.sql to create required tables
echo "Creating tables from fitness.sql..."
mysql -h "localhost" -u "root" -p"raghvendra" "gymdb" < fitness.sql || handle_error "Failed to execute fitness.sql"

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt || handle_error "Failed to install Python dependencies"

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput || handle_error "Failed to collect static files"

echo "Build completed successfully."
