#!/usr/bin/env python
import logging
import os
import random
import string

import requests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    logger.info(f"Random string of length {length} length, is: {result_str}")


def create_incident():
    pass
    try:
        # Set the request parameters
        url = 'https://myinstance.service-now.com/api/now/table/incident'
        user = os.environ['SNOW_USER']
        pwd = os.environ['SNOW_PWD']

        # Set proper headers
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = requests.post(url, auth=(user, pwd), headers=headers, data='{"short_description":"Test"}')

        # Check for HTTP codes other than 200
        if response.status_code != 201:
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
            exit()
        print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())

    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    create_incident()
    get_random_string(12)
