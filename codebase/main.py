import os

from openai import OpenAI

api_key = ""

client = OpenAI(
  api_key=api_key,
)

question = input("What is your question\n")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}
  ]
)

print(completion)
# print(completion.choices[0].messages.content)



