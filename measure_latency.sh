#!/bin/bash

# Set the connection details for Azure PostgreSQL
server="your_postgresql_server_name.postgres.database.azure.com"
database="your_database_name"
username="your_username"
password="your_password"

# Set the number of times to execute the query for averaging
num_iterations=10

# Install psql client if not already installed
if ! command -v psql &>/dev/null; then
    echo "Installing psql client..."
    sudo apt-get update
    sudo apt-get install -y postgresql-client
fi

# Execute the "Select 1" query and measure roundtrip time
total_time=0

for ((i=1; i<=num_iterations; i++)); do
    echo "Executing query $i of $num_iterations..."
    start_time=$(date +%s%N)  # Start time in nanoseconds
    
    # Connect to Azure PostgreSQL and execute the query
    result=$(PGPASSWORD=$password psql -h $server -U $username -d $database -c "SELECT 1;" 2>&1)
    exit_code=$?
    
    end_time=$(date +%s%N)  # End time in nanoseconds
    execution_time=$(( (end_time - start_time) / 1000000 ))  # Convert to milliseconds
    
    if [[ $exit_code -eq 0 ]]; then
        echo "Query executed successfully in $execution_time ms"
        total_time=$((total_time + execution_time))
    else
        echo "Query execution failed: $result"
    fi
done

# Calculate and display average roundtrip time
average_time=$((total_time / num_iterations))
echo "Average roundtrip time: $average_time ms"
