# Python Assignment

## Q1:In DevOps, ensuring strong security practices is essential for protecting systems and sensitive data.Enforcing a strong password policy is one key measure to prevent unauthorized access. The following explanation outlines how a Python program can be used to validate password strength based on several critical criteria.
Implementation:
Input and Function Definition:

The program defines a function check_password_strength that takes a password string as input.
This function validates the password against multiple security criteria and returns a tuple containing a boolean (indicating success or failure) and a message describing the result.
Password Criteria:

Minimum Length:
The password must be at least 8 characters long.
Uppercase and Lowercase Letters:
The password must contain both uppercase and lowercase letters. This ensures complexity and avoids simple patterns.
Digits:
At least one digit (0-9) must be included to add numerical complexity.
Special Characters:
The password must contain at least one special character (from a predefined set such as !@#$%^&*(),.?":{}|<>). This further strengthens the password against brute-force attacks.
Validation Process:

The function checks each of the criteria sequentially:
It first verifies the password length.
Then, it uses generator expressions to check for the presence of lowercase and uppercase letters.
It checks for digits using a similar approach.
Finally, it employs the re.search function from Python’s re module to determine if the password contains at least one special character.
If any of these checks fail, the function returns False along with an appropriate error message.
If all checks pass, the function returns True with the message "Password is strong!"
User Interaction:

In the main block of the script, the user is prompted to enter a password.
The input password is passed to the check_password_strength function, and based on the returned boolean, the program prints either a success message (with a check mark) or an error message (with a cross mark).

Output: 
  * Code checks the leagnth of tha Passwd.
    - ![image](https://github.com/user-attachments/assets/3bc70ef0-dcdc-41da-9c97-a7b65962107d)
      
  * Code checks passwd upper and lower case criteria.
    - ![image](https://github.com/user-attachments/assets/306c6bd8-f2ad-4fa5-ae77-de2f6f7328ca)
      
  * Code checks the digit criteria.
    - ![image](https://github.com/user-attachments/assets/1a37ef5a-3ada-4da7-a136-8d372bfe5424)
  
  * Code checks the Special Character criteria.
    - ![image](https://github.com/user-attachments/assets/fae0752d-a268-442b-9e86-1f8f849fcb82)
    
  * Final Ouput, if mainatian the required criteria.
     - ![image](https://github.com/user-attachments/assets/7fcc5a85-8f6f-42da-b644-964263c61b55)


 
  


### Q2:In DevOps, monitoring the health and performance of servers is crucial for ensuring smooth operation of infrastructure.

Implementation:

Continuously Monitor CPU Usage:
Use the psutil library in Python to fetch the CPU usage percentage. The program repeatedly checks the CPU usage at a set interval (e.g., every 1 second).

Trigger Alerts When Usage Exceeds Threshold:
If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message is displayed indicating that the CPU usage is too high.

Run Indefinitely Until Interrupted:
The program uses a while loop to continuously monitor the CPU usage. It runs indefinitely until it is manually interrupted (e.g., by pressing Ctrl+C).

Error Handling:
The program includes error handling (via a try-except block) to gracefully catch interruptions and display a shutdown message.

Output: For testing the code threshold value changed to 1
- ![image](https://github.com/user-attachments/assets/33265a46-184a-40fd-a5c4-5976deafabe6)


#### Q3: Configuration File Parsing in DevOps?

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




