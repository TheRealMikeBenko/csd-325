# Michael Benko
# 2026-09-22
# CSD325-302E Advanced Python (2267-DD)
# Module 9.2 Assignment

# This program demonstrates how to connect to an API with Python and show the raw and formatted JSON data.
# Exemption handling is included to manage any potential errors that may arise during the API request.
# Non-required improvements made to the output to make it more readable and user-friendly.

import requests
import json

def jprint(obj):
    # Create a formatted string of the Python JSON object.
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def main():
    try:
        response = requests.get("https://anapioficeandfire.com/api/characters/583") # Make a GET request to the API endpoint.
        print(f"Response Status Code: {response.status_code}\n") # Print the status code of the response.
        if response.status_code == 200:
            print(f"Raw JSON: \n{response.json()}\n") # Raw JSON
            print("Formatted JSON:")
            jprint(response.json()) # Formatted JSON
        
    except requests.RequestException: # Handle any exceptions that occur during the API request.
        print(f"Error fetching API data.") # I did not include the error message in the print statement to avoid long outputs.

# Call the main function to start the program.
if __name__ == "__main__":
    main()