import os
import openai
openai.api_key = ""

# This Chatbot class from Test1.py successfully implements 
# the ChatGPT API to respond in varying degrees of helpfulness.
class Chatbot:
  result = "temp"


  question  = input("What is your question?")

  level = input("On a scale of 1 - 3, how helpful would you like my response to be?")
  rude = input("Would you like a rude response?")

  if level == "1":
    result = question

  elif level == "2":
    result = "Respond to this in the most unhelpful way as possible:" + question

  elif level == "3":
    result = "Repeat this statement exactly as follows: The probability of a snowflake being identical to another is about 1 in 10^18."

  elif level !="1" and level !="2" and level !="3":
    result = "Repeat this statement exactly as follows: That is not a valid response!"


  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": result}
    ]
  )

  response = completion.choices[0].message.content # for adding into the message box

  print(completion.choices[0].message.content)