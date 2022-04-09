"""
    Authors: Louis You & Jee Kim
    Purpose: Main file for the spotify project
"""
import secrets
import requests

if __name__ == "__main__":
    print("Hello World!")

    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)


    # print(secrets.CLIENT_ID)


"""
    How do we authenticate ourselves

    (1) Send a (POST/GET) request to get to the correct endpoint
    (2) Send out package (secrets CLIENTID/Secret)
    (3) Response is sent by SPOTIFY (failed/suceeded/error)
    (4) Read the response and if it is authenticated then we move on
"""
