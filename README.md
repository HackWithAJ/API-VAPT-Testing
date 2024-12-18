# VAPT API Testing

This repository contains a Python script for performing VAPT (Vulnerability Assessment and Penetration Testing) on APIs. The script integrates Postman collection execution and performs a series of vulnerability tests on APIs, such as authentication attacks, authorization bypass, sensitive data exposure, and IDOR (Insecure Direct Object Reference).

## Features

- **Run Postman Collections**: Executes Postman collections using `newman`.
- **Authentication Testing**: Tests for weak passwords and attempts to bypass authentication.
- **Authorization Testing**: Checks for unauthorized access using invalid tokens.
- **Sensitive Data Exposure**: Verifies that sensitive information is not exposed in API responses.
- **IDOR (Insecure Direct Object Reference)**: Tests for unauthorized access to resources based on user IDs.

## Prerequisites

1. **Node.js and npm**: Required to install Postman's `newman` CLI. Download Node.js from [https://nodejs.org/](https://nodejs.org/).
2. **Python 3.x**: Install Python 3 from [https://www.python.org/downloads/](https://www.python.org/downloads/).
3. **Newman**: Install Newman globally using npm.

   ```bash
   npm install -g newman

## Install Python Dependencies

You will need the following Python packages:

- **requests**: To send HTTP requests.
- **pytest**: For testing (optional, in case you want to add automated tests).

You can install them using **pip**:

```bash
pip install -r requirements.txt

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/vapt-api-testing.git
   cd vapt-api-testing

