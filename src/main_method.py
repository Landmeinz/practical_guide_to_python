
# try: 
#     print("sup")
# finally:
#     print("yup that worked")


# # setup VIRTUAL ENVIRONMENTS

# # run: python -m venv env
# # run: source env/bin/activate

# # run: pip freeze > requirements.txt
# # run: pip install -r requirements.txt

# import random
# print('--- a random number:', random.randint(0, 100))

# from random import randint
# print('--- another way:', randint(0, 50))

# import datetime

# put code in a modules folder to keep organized

# unit testing is built in 

# pypi.org;  you can browse packages to install with pip


# MAKE SURE YOU ARE IN THE (ENV:VENV)

# # First thing we'll do is import the requests library
# import requests

# # Define a variable with the URL of the API
# api_url = "http://shibe.online/api/shibes?count=1"

# # Call the root of the api with GET, store the answer in a response variable
# # This call will return a list of URLs that represent dog pictures
# response = requests.get(api_url)
# print('--- the response', response)

# # Get the status code for the response. Should be 200 OK
# # Which means everything worked as expected
# # print(f"Response status code is: {response.status_code}")

# # Get the result as JSON
# response_json = response.json()

# # Print it. We should see a list with one image URL.
# print(response_json)


# First thing we'll do is import the requests library
import requests

# We'll store our base URL here and pass in the count parameter later
api_url = "http://shibe.online/api/shibes"

params = {
   "count": 10
}

# Pass those params in with the request.
api_response = requests.get(api_url, params=params)

print(f"Shibe API Response Status Code is: {api_response.status_code}")  # should be 200 OK

json_data = api_response.json()

print("Here is a list of URLs for dog pictures:")
for url in json_data:
    print(f"\t {url}")
