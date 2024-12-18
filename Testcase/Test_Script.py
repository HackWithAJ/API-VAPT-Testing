import requests
import json
import subprocess
import os
import sys
import platform

# Define the VAPTTesting class to perform VAPT tasks
class VAPTTesting:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def send_request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        try:
            if method.lower() == 'get':
                response = requests.get(url, headers=self.headers, params=params)
            elif method.lower() == 'post':
                response = requests.post(url, headers=self.headers, data=data)
            elif method.lower() == 'put':
                response = requests.put(url, headers=self.headers, data=data)
            elif method.lower() == 'delete':
                response = requests.delete(url, headers=self.headers)
            else:
                raise ValueError("Invalid HTTP method")
            return response
        except Exception as e:
            print(f"Error sending request: {e}")
            return None

    # Authentication Attack (Test for weak passwords)
    def test_authentication(self, endpoint, username, weak_passwords):
        for password in weak_passwords:
            data = {'username': username, 'password': password}
            response = self.send_request('post', endpoint, data=data)
            if response and response.status_code == 200:
                print(f"Authentication bypassed with password: {password}")
            else:
                print(f"Authentication failed for password: {password}")

    # Authorization Attack (Test unauthorized access)
    def test_authorization(self, endpoint, user_token, invalid_token):
        response_valid = self.send_request('get', endpoint, headers={'Authorization': f'Bearer {user_token}'})
        if response_valid and response_valid.status_code == 200:
            print("Authorized access with valid token.")

        response_invalid = self.send_request('get', endpoint, headers={'Authorization': f'Bearer {invalid_token}'})
        if response_invalid and response_invalid.status_code == 403:
            print("Unauthorized access prevented with invalid token.")
        else:
            print("Authorization vulnerability detected, invalid token accepted.")

    # Sensitive Data Exposure (Check if sensitive data is exposed in responses)
    def check_sensitive_data(self, response, sensitive_keys):
        for key in sensitive_keys:
            if key in response.text:
                print(f"Sensitive data exposure detected: {key} found in response.")
            else:
                print(f"No sensitive data exposed for: {key}.")

    # IDOR (Insecure Direct Object Reference) Testing
    def test_idor(self, endpoint, valid_user_id, unauthorized_user_id):
        response_valid = self.send_request('get', endpoint + f'/{valid_user_id}', headers=self.headers)
        if response_valid and response_valid.status_code == 200:
            print(f"Access granted to resource for user ID: {valid_user_id}")

        response_invalid = self.send_request('get', endpoint + f'/{unauthorized_user_id}', headers=self.headers)
        if response_invalid and response_invalid.status_code == 403:
            print(f"Access denied to resource for unauthorized user ID: {unauthorized_user_id}")
        else:
            print(f"IDOR vulnerability detected, unauthorized access allowed for user ID: {unauthorized_user_id}")


# Function to run Postman collection using newman
def run_postman_collection(collection_file_or_url):
    # Check the operating system and set appropriate subprocess arguments
    if platform.system() == "Windows":
        shell_command = ['newman', 'run', collection_file_or_url]
    else:
        shell_command = ['newman', 'run', collection_file_or_url]

    try:
        result = subprocess.run(
            shell_command,
            capture_output=True,
            text=True,
            shell=True  # This is critical for Windows to run shell commands
        )
        if result.returncode != 0:
            print(f"Error running Postman collection: {result.stderr}")
        else:
            print("Postman collection executed successfully.")
            print(result.stdout)
    except Exception as e:
        print(f"Error running Postman collection: {e}")


# Function to take input from the user and execute tests
def main():
    # Get the Postman collection file or URL from the user
    collection_input = input("Enter the Postman collection file path or URL: ").strip()

    # Check if the collection input is valid (file or URL)
    if not os.path.exists(collection_input) and not collection_input.startswith("http"):
        print("Invalid file path or URL.")
        return

    # Ensure paths are in the correct format for the current operating system
    collection_input = os.path.normpath(collection_input)

    # Run the Postman collection using newman
    run_postman_collection(collection_input)

    # Ask if the user wants to run VAPT testing
    run_vapt = input("Would you like to perform VAPT testing (y/n)? ").lower()
    
    if run_vapt == 'y':
        # Get the base URL and tokens
        base_url = input("Enter the base API URL: ").strip()
        valid_token = input("Enter a valid token: ").strip()
        invalid_token = input("Enter an invalid token: ").strip()

        # Example user for authentication and IDOR tests
        username = input("Enter username for authentication testing: ").strip()
        weak_passwords = input("Enter weak passwords (comma separated): ").split(',')

        sensitive_keys = input("Enter sensitive keys to check for exposure (comma separated): ").split(',')
        
        # Initialize the VAPTTesting class
        api_tester = VAPTTesting(base_url=base_url, headers={'Content-Type': 'application/json'})
        
        # Run Authentication Attack
        api_tester.test_authentication('/login', username=username, weak_passwords=weak_passwords)
        
        # Run Authorization Attack
        api_tester.test_authorization('/profile', user_token=valid_token, invalid_token=invalid_token)
        
        # Run Sensitive Data Exposure Test
        response = api_tester.send_request('get', '/user/123', headers={'Authorization': f'Bearer {valid_token}'})
        api_tester.check_sensitive_data(response, sensitive_keys=sensitive_keys)
        
        # Run IDOR Attack
        valid_user_id = input("Enter a valid user ID for IDOR testing: ").strip()
        unauthorized_user_id = input("Enter an unauthorized user ID for IDOR testing: ").strip()
        api_tester.test_idor('/user', valid_user_id=valid_user_id, unauthorized_user_id=unauthorized_user_id)

# To run the script
if __name__ == "__main__":
    main()
