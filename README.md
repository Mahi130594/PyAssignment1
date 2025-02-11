# Python Assignment

## Q3: Configuration File Parsing in DevOps

In DevOps, managing configuration files is crucial for automating infrastructure and ensuring consistency. Configuration files store essential settings, such as database credentials, server addresses, and application parameters. Automating the parsing of these files helps maintain uniformity and reduces manual errors.

Implementation:

Read a configuration file containing key-value pairs.

Extract relevant settings and store them in a structured data format like a dictionary.

Handle errors gracefully if the file is missing or unreadable.

Convert the extracted information into JSON format and save it to a database.

Provide a GET API to fetch the stored configuration data.

Sample Configuration File:

[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080

Output:
- ![image](https://github.com/user-attachments/assets/c41a65f5-2a34-4755-9ccc-aa0989ad46c2) - ![image](https://github.com/user-attachments/assets/202d42f7-c021-4f1a-8c66-9eb24caeb1b0)



