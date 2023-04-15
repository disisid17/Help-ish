import os
import openai
openai.api_key = "*******************************************"



question = input("What do you need help with?\n")
rephrase = "Respond to this in the most unhelpful way possible: " + question
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": rephrase}
  ]
)


print(completion.choices[0].message.content)
