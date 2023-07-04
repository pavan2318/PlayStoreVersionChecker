##################################################
#                                                #
#    PlayStoreVersionChecker Script               #
#                                                #
#    Version: 0.1                                #
#    Developed by: Pavan                         #
#    GitHub: https://github.com/pavan2318/       #
#                                                #
##################################################

# Usage: python playstore_version_checker.py
# -------------------------------------------
# This script retrieves the current running version of an application on the Google Play Store.
# It prompts the user to enter the Google Play Store URL for the application and then fetches
# the version information from the Play Store webpage's response.

# Prerequisites:
# - Python 3.x
# - Requests library (Install using 'pip install requests')
# - Beautiful Soup library (Install using 'pip install beautifulsoup4')

# Changelog:
# -------------------------------------------
# Version 0.1 (2023-07-01):
# - Initial release of PlayStoreVersionChecker
# - Added functionality to retrieve the current running version
# - Implemented parsing of HTML response to extract version information
# - Provided a command-line interface for user interaction
# - Supported customization of the Play Store URL
import requests
import re

# Accept URL from the user
url = input("Enter the Google Play Store URL for the application: ")

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the version number using regex
    version_pattern = r"\[\"(\d+\.\d+\.\d+)\"\]"
    match = re.search(version_pattern, response.text)

    if match:
        # Extract the version value
        version = match.group(1)
        print("Current running version:", version)
    else:
        print("Version number not found.")
else:
    print("Error:", response.status_code)
