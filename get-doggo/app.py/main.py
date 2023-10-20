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
import httpx


# Initailize the FastAPI application
app = FastAPI()

# Initailize variables to contain the API endpoint, the image returned from the API, and the HTML code to display the image to the user
api_endpoint = "https://shibe.online/api/shibes?count=1"
image_link = ""
image = ""

# Define main function to get the image link from the API (in JSON) then make a request to that returned link to get the image (in bytes)
async def get_doggo():

    # Declare global variables
    global image_link, api_endpoint, image

    # Make a request to the API endpoint
    async with httpx.AsyncClient() as client:
        response = await client.get(api_endpoint)

    # Check if the request was successful
    if response.status_code == 200:

        # Get the image link from the JSON response
        image_link = response.json()[0]

        # Make a request to the image link
        image = requests.get(image_link).content

    # If the request was not successful, raise an HTTPException
    else:
        raise HTTPException(status_code=response.status_code, detail="Error: Could not get image from API")

    return image_link, image

# Define a a default router that will display the image to the user we got earlier using HTMLResponse
@app.get("/", response_class=HTMLResponse, summary="The default route for the application.")
async def default_route():
    
        # Get the image link and image
        get_doggo()
    
        # Create the HTML code to display the image to the user
        html_content = f"""
        <html>
            <head>
                <title>Get Doggo</title>
            </head>
            <body>
                <h1>Get Doggo</h1>
                <img src="{image_link}" alt="A random image of a Shiba Inu dog.">
                <br>
                <button onclick="window.location.reload();">Get New Image</button>
            </body>
        </html>
        """
    
        # Return the HTML code to the user
        return HTMLResponse(content=html_content)




