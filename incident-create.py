#!/usr/bin/env python
import logging
import os
import random
import string
import json
import sys
import requests

# Set the logging to the lowest level
logging.basicConfig(level=logging.ERROR)
# Allocate a logger
logger = logging.getLogger(__name__)


class CreateIncident:

    def __init__(self):
        self._user = os.environ['SNOW_USER']
        self._pwd = os.environ['SNOW_PWD']
        self._instance = os.environ['SNOW_INSTANCE']

    #
    # Helper function to generate a string of any length
    #
    @staticmethod
    def get_random_string(string_length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(string_length))
        logger.debug(f"Random string of length {string_length} length, is: {random_string}")
        return random_string

    def get_user_id(self, user_name):
        url = f"https://{self._instance}.service-now.com/api/now/table/sys_user?sysparm_limit=1&user_name={user_name}"
        # Set proper headers
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, auth=(self._user, self._pwd), headers=headers)
        response.raise_for_status()
        logger.info(f"Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}")
        doc = response.json()
        return doc['result'][0]['sys_id']

    #
    # Function that creates an incident in ServiceNOW
    # using requests library
    #
    def create_incident(self, short_description, caller):
        pass
        try:
            caller_id = self.get_user_id(caller)

            # Set the request parameters
            url = f"https://{self._instance}.service-now.com/api/now/table/incident"

            # Set proper headers
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            incident = {
               "short_description": short_description,
               "caller_id": caller_id
            }
            data = json.dumps(incident)
            response = requests.post(url, auth=(self._user, self._pwd), headers=headers, data=data)
            response.raise_for_status()
            logger.info(f"Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}")

            print(json.dumps(response.json(), sort_keys=True, indent=2))

        except Exception as e:
            logger.exception(e)


def main():
    if len(sys.argv) == 2:
        caller = sys.argv[1]
        incident = CreateIncident()
        random_string = CreateIncident.get_random_string(32)
        incident.create_incident(short_description=random_string, caller=caller)
    else:
        print(f"usage: {os.path.basename(sys.argv[0])} name")


if __name__ == '__main__':
    main()
