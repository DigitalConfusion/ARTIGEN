from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

api = os.getenv('OPENAI_API_KEY')
print(api)
from openai import OpenAI
client = OpenAI(
  api_key=api
)

response = client.images.generate(
  model="dall-e-2",
  prompt="line art of a white siamese cat",
  size="256x256",
  quality="standard",
  n=1,
)

image_url = response.data[0].url