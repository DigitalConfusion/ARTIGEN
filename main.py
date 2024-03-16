from dotenv import load_dotenv
from openai import OpenAI
from chatgpt import callGPT3
from reddit import getTitles
from datetime import datetime
from PIL import Image          # pillow, for processing image types
import PIL              # for decoding images if recieved in the reply
import os
load_dotenv()

api = os.getenv('OPENAI_API_KEY')
print('\n\n\n\n\n\n')
from openai import OpenAI
client = OpenAI(
  api_key=api
)
redditPrompt = getTitles()
generatedPrompt = callGPT3(redditPrompt)
response = client.images.generate(
  model="dall-e-3",
  prompt=generatedPrompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

# Now you can download the image and save it using its URL
import requests

image_response = requests.get(image_url)

if image_response.status_code == 200:
    with open(f"bildeCool_{datetime.now().strftime('%H.%M')}.png", "wb") as image_file:
        image_file.write(image_response.content)
    print("bildeCool.png was saved")
else:
    print("Failed to download image.")