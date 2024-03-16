def callGPT3(text):
  # Importing the openai module
  # from reddit import getTitles
  from openai import OpenAI
  import os
  from dotenv import load_dotenv
  load_dotenv()
  # Setting the API key
  api = os.getenv('OPENAI_API_KEY')

  client = OpenAI(
    api_key=api
  )
  # Creating the OpenAI GPT-3 client
  prompt = '\n'.join(text) + "\n generate a promt for dalle-3 by choosing the easiest headline to visualise using a simple one line artstyle."

  gpt3 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a promt generating machine that creates a Dalle-3 promt. Your goal is to create a promt for a simple art"},
      {"role": "user", "content": prompt}
    ]
  )
  print(gpt3.choices[0].message.content)
  value = '''Try visualizing this headline with a simple one-line art style depicting an elderly person with a smile,
  delivering a meal to a person in need.'''
  return(gpt3.choices[0].message.content)

# Ja mees launchojam tik sho failu, tad izprinte promptu ar tadu tekstu
callGPT3([
    "Snake",
    "Jelly donuts",
    "Mechanic Witch",
    "Gazing",
    "Incapacitated"
])