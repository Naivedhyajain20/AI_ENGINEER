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

#structure formate
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    mobile_number:int
    reason: str
    address:str

schema = Ticket.model_json_schema()

response_formate ={
    "type" : "json_object"
}

system_prompt = f"""
 Extract the info from the ticket strictly based on schema and give me the output in json format only.
 {schema}
"""

system_message = {
    "role" : "system",
    "content" : system_prompt
}

text = " My samsung phone got broken due to lack of display in components.My name is SUSU MUDHU and my address is soya hua munga 005, and my phone no. is 69696"
prompt = f"""
This is the costumer ticket , please extract the info like name , mobile no. , reason , address and give me.
{text}
"""
message = {
    "role": role,
    "content": prompt
    }
messages = [system_message , message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_formate)
print(response)


answer = response.choices[0].message.content
print(answer)

#isko padhte kaise hai

import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.address)
print(ticket.mobile_number)
print(ticket.reason)
print(ticket.name)
