from dotenv import load_dotenv
from openai import OpenAI
from chatgpt import callGPT3
from reddit import getTitles
import os
load_dotenv()

api = os.getenv('OPENAI_API_KEY')
print('\n\n\n\n\n\n')
from openai import OpenAI
client = OpenAI(
  api_key=api
)
redditPrompt = getTitles()
generatedPromt = callGPT3(redditPrompt)
response = client.images.generate(
  model="dall-e-2",
  prompt=generatedPromt,
  size="256x256",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)