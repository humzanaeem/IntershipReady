import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.nasa.gov/planetary/apod?api_key="
unique_key = os.getenv("NASA_API_KEY")


def apod_generator(url, key):
    final_url = url + key
    response = requests.get(final_url).json()
    return response


