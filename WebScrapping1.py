# This code issues an HTTP GET request to the given URL.
# It retrieves the HTML data that the server sends back and stores that data in a Python object.


import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)