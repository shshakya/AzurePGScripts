# PostgreSQL Server Settings Diff

A Python script to compare the settings of two PostgreSQL servers and display the differences between them.

## Prerequisites

To run this script, you need to have the following installed:

- Python (version 3 or higher)
- psycopg2 library (install via `pip install psycopg2`)

## Usage

1. Clone this repository to your local machine or download the script file directly.

2. Open the script file `server_settings_diff.py` in a text editor.

3. Modify the connection details for the first PostgreSQL server (`host1`, `port1`, `database1`, `user1`, `password1`) and the second PostgreSQL server (`host2`, `port2`, `database2`, `user2`, `password2`) with the appropriate values.

4. Save the changes to the script file.

5. Open a terminal or command prompt and navigate to the directory where the script file is located.

6. Run the script using the following command:

  ```bash
  python server_settings_diff.py
  ```

7. The script will compare the parameters between the two servers and display the following sections:

-   Differences between server1 and server2:
    
    -   Lists the parameters that have different settings between the servers.
-   Parameters existing on server1 but not on server2:
    
    -   Lists the parameters that exist on server1 but not on server2, along with their settings from server1.
-   Parameters existing on server2 but not on server1:
    
    -   Lists the parameters that exist on server2 but not on server1, along with their settings from server2..

## Note

- Make sure you have proper network connectivity and access privileges to the PostgreSQL servers you want to compare.
- The script assumes that both PostgreSQL servers have the same table (`pg_settings`) with the columns `name` and `setting`. Modify the SQL statements in the script if your servers have different table or column names.
