import os
import openai
openai.api_key = "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" #remove key when uploading to github



question = input("What do you need help with?\n")
rephrase = "Respond to this in the most unhelpful way possible: " + question
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": rephrase}
  ]
)


print(completion.choices[0].message.content)
