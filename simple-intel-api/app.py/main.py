'''

This sample application will query this API endpoint:
https://shibe.online/api/shibes?count=1

Which gets a random image of a Shiba Inu dog. The application will then display the image to the user in the browser.

A single "Get New Image" button will be the only button that the person can click on. When the button is clicked, the application will query the API endpoint again and display the new image to the user.
The backend will be done exclusively in FastAPI using the HTMLResponse class to display the image to the user so that the project exists in one main.py file and no reliance on external file is needed.



Designed as an example for James and Alec's Experiements repo for future projects.

'''


# Import required libraries
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
import requests
import re
import threading


# Initailize the FastAPI application
app = FastAPI()

# Initailize variables to contain the API endpoint, the image returned from the API, and the HTML code to display the image to the user
api_endpoint = "https://shibe.online/api/shibes?count=1"
image_link = ""
image = ""
html_code = ""

# Define main function to get the image link from the API (in JSON) then make a request to that returned link to get the image (in bytes)
def get_doggo():




