[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
![use-wisely](https://user-images.githubusercontent.com/79195338/161229028-2d3acfde-8028-45bc-ba1a-a397f0bc46e3.svg)

# VAPT API Testing Automation Script By HackWithAJ

This repository contains a Python script for performing **VAPT** (Vulnerability Assessment and Penetration Testing) on APIs. The script integrates **Postman collection execution** and performs a series of vulnerability tests on APIs, such as **authentication attacks**, **authorization bypass**, **sensitive data exposure**, and **IDOR** (Insecure Direct Object Reference).

![Vulnerability Testing Illustration](./API-VAPT-Testing/VAPT.png)


## Features

- **Run Postman Collections**: Executes Postman collections using **newman**.
- **Authentication Testing**: Tests for weak passwords and attempts to bypass authentication.
- **Authorization Testing**: Checks for unauthorized access using invalid tokens.
- **Sensitive Data Exposure**: Verifies that sensitive information is not exposed in API responses.
- **IDOR (Insecure Direct Object Reference)**: Tests for unauthorized access to resources based on user IDs.

## Prerequisites

Before running the tests, make sure you have the following software installed:

1. **Node.js and npm**: Required to install Postman's **newman** CLI. Download Node.js from https://nodejs.org/.
2. **Python 3.x**: Install Python 3 from https://www.python.org/downloads/.
3. **Newman**: Install **Newman** globally using npm:

   ```bash
   npm install -g newman
   ```

### Install Python Dependencies

You will need the following Python packages:

- `requests`: To send HTTP requests.
- `pytest`: For testing (optional, in case you want to add automated tests).

You can install them using pip:

```bash
pip install -r requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/vapt-api-testing.git
cd vapt-api-testing
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Ensure that newman is installed:

```bash
npm install -g newman
```

## Running the Tests

### On Windows

You can easily run the tests by executing the provided batch file `run_tests.bat`. This will automatically install the necessary Python dependencies, execute the Postman collection, and run the VAPT testing:

Double-click the `run_tests.bat` file or run it from the Command Prompt:

```bash
run_tests.bat
```

### On Linux or macOS

On Linux/macOS, you can run the Python script directly:

```bash
python3 test_vapt.py
```

During execution, the script will prompt you for the following inputs:

- **Postman Collection File or URL**: Provide the file path or a URL to the Postman collection you want to test.
- **Base API URL**: The base URL of your API (e.g., `http://localhost:3000`).
- **Valid Token**: Provide a valid token for authorization testing.
- **Invalid Token**: Provide an invalid token for testing unauthorized access.
- **Username for Authentication Testing**: Provide a username for testing weak passwords.
- **Weak Passwords**: List weak passwords to test (comma-separated).
- **Sensitive Data Keys**: Provide keys that might represent sensitive data (comma-separated).
- **User IDs for IDOR Testing**: Enter a valid and unauthorized user ID to check for IDOR vulnerabilities.

### Example Usage

When prompted, provide the necessary information:

```bash
Enter the Postman collection file path or URL: /path/to/collection.json
Would you like to perform VAPT testing (y/n)? y
Enter the base API URL: http://localhost:3000
Enter a valid token: validtoken123
Enter an invalid token: invalidtoken123
Enter username for authentication testing: admin
Enter weak passwords (comma separated): password123, 12345, qwerty
Enter sensitive keys to check for exposure (comma separated): password, token
Enter a valid user ID for IDOR testing: 1
Enter an unauthorized user ID for IDOR testing: 2
```

### What Happens During the Tests?

The following VAPT checks will be performed automatically:

- **Authentication Testing**: The script will test for weak passwords by attempting to log in with various common passwords.
- **Authorization Testing**: It will test whether the API correctly rejects access with an invalid token and accepts access with a valid token.
- **Sensitive Data Exposure**: The script checks if sensitive information, like passwords or tokens, is exposed in API responses.
- **IDOR Testing**: It tests whether unauthorized users can access resources intended for others by using different user IDs.
