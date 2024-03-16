def callGPT3(text):
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
  prompt = '\n'.join(text) + "\n Choose the best headline (only one) to visualize as art using a simple one line art style and make a promt out of it."

  gpt3 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Your task is to generate a prompt for creating simple one-line art. The prompt should guide the user to choose the best headline from a list and visualize it as art using a one-line drawing style and draw only outlines."},
      {"role": "user", "content": prompt}
    ]
  )
  a = (gpt3.choices[0].message.content)
  print("\n\n\n\n\n", gpt3.choices, "\n\n\n\n\n\n")
  print(a)
  return(a)

# Ja mees launchojam tik sho failu, tad izprinte promptu ar tadu tekstu
callGPT3([
    "Alien",
    "Crazy monster",  
    "Snake",
    "Jelly donuts",
    "Mechanic Witch",
    "Gazing",
    "Incapacitated"
])