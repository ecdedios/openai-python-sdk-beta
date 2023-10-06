import os
from dotenv import load_dotenv
import openai

load_dotenv()
MY_ENV_VAR = os.getenv('OPENAI_API_KEY')

openai.api_key = MY_ENV_VAR

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
