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
# 3 prompts
prompt1 = "hi!!"
prompt2 = "Explain time travel in detail under 100 words"
prompt3 = "write 1000 words eassy on Machine Learning"
prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
    "role": role,
    "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages , max_tokens=50 )
    usage = response.usage
    print(f"Prompt :{prompt} --> prompt tokens: {usage.prompt_tokens} completion_tokens --> {usage.completion_tokens} total_tokens--> {usage.total_tokens} Finish Reasone : {response.choices[0].finish_reason }") 
