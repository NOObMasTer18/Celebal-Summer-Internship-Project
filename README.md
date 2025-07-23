# Celebal Summer Internship Project

This repository contains the solution for the following project problem statement:

## Problem Statement

1. **Establish connectivity with a SQL Server database using Python.**  
   The database is hosted on a remote server, and you need to provide the necessary credentials to establish the connection.

2. **Design a Python script to connect to the SQL Server database, retrieve data from a specific table named "Employees", and print the first 5 rows of the table.**

3. **Create a Python script that:**
   - Establishes a connection to the SQL Server database using the provided credentials.
   - Retrieves data from the "Employees" table.
   - Prints the first 5 rows of the table.
   - Handles any potential errors that may occur during the connection process and data retrieval.

   You may use any appropriate Python libraries for connecting to SQL Server and handling database operations.

## Requirements

- The SQL Server database is hosted on a remote server with the IP address: `4.240.94.220`
- Database name: `CompanyDB`
- Table name: `Employees`
- Credentials:
  - Username: `YourUsername`
  - Password: `YourPassword123`

## Solution Overview

The solution consists of a Python script that uses the following libraries:
- [`pyodbc`](https://github.com/mkleehammer/pyodbc) or another suitable driver for SQL Server connectivity.
- [`python-dotenv`](https://github.com/theskumar/python-dotenv) and `os` for securely loading credentials and configuration from an `.env` file.
- [`tabulate`](https://github.com/astanin/python-tabulate) for pretty-printing the fetched employee data in tabular format.

The script:
- Loads database connection details from an `.env` file for security.
- Connects to the remote SQL Server database using these credentials.
- Executes a SQL query to fetch the first 5 rows from the `Employees` table.
- Prints the results in a readable table.
- Handles exceptions related to connection failures and data retrieval errors.

## Usage Instructions

1. **Install Dependencies**

   Make sure you have Python installed.  
   Install the required libraries:

   ```bash
   pip install pyodbc python-dotenv tabulate
   ```

2. **Configure Environment Variables**

   Create a file named `.env` in the project directory with the following content:

   ```
   SQL_SERVER=4.240.94.220
   SQL_DATABASE=CompanyDB
   SQL_USERNAME=YourUsername
   SQL_PASSWORD=YourPassword123
   ```

3. **Run the Script**

   Execute the Python script:

   ```bash
   python connect_sqlserver_and_fetch_first_5_records.py
   ```

   The script will print the first 5 rows from the `Employees` table in a well-formatted table.

## Notes

- Ensure the required ODBC driver for SQL Server is installed on your system.
- Never commit your `.env` file or credentials to version control.
- Handle credentials securely and avoid exposing sensitive data.

## License

This project is for educational and demonstration purposes as part of the Celebal Summer Internship.
