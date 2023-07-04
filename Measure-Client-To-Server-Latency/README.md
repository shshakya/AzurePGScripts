# Azure PostgreSQL Latency Measurement

This script allows you to measure the roundtrip time of executing a query on an Azure PostgreSQL database and calculate the average roundtrip time. It utilizes the psql client to connect to the database and execute the query multiple times.

## Prerequisites

Before running this script, ensure that you have the following information available:

- Azure PostgreSQL server name: Replace `your_postgresql_server_name` in the script with your actual server name.
- Database name: Replace `your_database_name` with the name of your database.
- Username and password: Replace `your_username` and `your_password` with your database credentials.

## Installation

Make sure you have the psql client installed. If not, the script will install it for you using the following command:

```shell
sudo apt-get update
sudo apt-get install -y postgresql-client
```

## Usage

1.  Replace the placeholders (`your_postgresql_server_name`, `your_database_name`, `your_username`, `your_password`) in the script with your actual Azure PostgreSQL server details.
    
2.  Save the script in a file, e.g., `measure_latency.sh`.
    
3.  Give the script executable permissions:

```shell
chmod +x measure_latency.sh
```
4. Run the script:

```shell
./measure_latency.sh
```
The script will execute the "Select 1" query multiple times, measure the roundtrip time, and calculate the average roundtrip time. The number of iterations is defined by the num_iterations variable in the script (default is 10).

## Output

The script will output the following information:

-   For each iteration, it will display the execution time of the query in milliseconds.
-   If the query execution fails, it will display the error message.
-   After all iterations, it will calculate and display the average roundtrip time.

Note: The script assumes you are running it on a Unix-like system with the `bash` shell.

