from dotenv import load_dotenv
from openai import OpenAI
from chatgpt import callGPT3
import os
load_dotenv()

api = os.getenv('OPENAI_API_KEY')
print('\n\n\n\n\n\n')
from openai import OpenAI
client = OpenAI(
  api_key=api
)
generatedPromt = callGPT3(["Dolph Lundgren and Wife Emma Krokdal Officially Become U.S. Citizens: 'It's About Time' (Exclusive)",
    "Ex-McLaren Engineer Reveals Childhood Sexual Abuse To Empower Others"])
response = client.images.generate(
  model="dall-e-2",
  prompt=generatedPromt,
  size="256x256",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)