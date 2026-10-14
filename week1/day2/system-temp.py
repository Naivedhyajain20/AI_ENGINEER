import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY kaha hai bhai?????")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

role = "user"
prompt = "i want to make a project for my resume tell me best project in aiml which also boost up my ats score of resume overall"
# system ka role and content 
message_system = {
    "role" : "system",
    "content" : "you are senior developer of ai and ml and have all the knoledge of it ."
}
# message mai role and content 
message = {
    "role": role,
    "content": prompt
    }

messages = [message_system , message]
# temprature is by default = 0
response = client.chat.completions.create(model=model, messages=messages, temperature=2 )
print(response)

print("#################################")

answer = response.choices[0].message.content
print(answer)
    