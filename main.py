from dotenv import load_dotenv
from openai import OpenAI
from chatgpt import callGPT3
import os
load_dotenv()

api = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key=api
generatedPromt = callGPT3()

response = client.images.generate(
  model="dall-e-2",
  prompt=generatedPromt,
  size="256x256",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)