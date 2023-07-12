
## Overview

The AutoVacuum Tuning Script is a Python program designed to automate the tuning of AutoVacuum parameters on a per-table basis. It allows users to specify the desired frequency at which AutoVacuum should be invoked on specific tables and monitors the row count changes to dynamically adjust the threshold when necessary.

AutoVacuum is a PostgreSQL feature that manages the cleanup and optimization of database tables to maintain performance and prevent table bloat. By default, AutoVacuum operates at the database level, but this script enables fine-grained control by allowing users to set AutoVacuum parameters on individual tables.

## Features

-   **Per-Table AutoVacuum**: Set AutoVacuum parameters on a per-table basis.
-   **Dynamic Threshold Adjustment**: Monitor row count changes and adjust the threshold when needed.
-   **Frequency-Based Invocations**: Specify the desired frequency at which AutoVacuum should be invoked on each table.
-   **Configurable Parameters**: Customize the AutoVacuum parameters based on your specific requirements.
-   **Automated Script**: Schedule the script to run periodically using cron or any other scheduling mechanism.
