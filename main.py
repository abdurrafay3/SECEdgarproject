import os
from openai import OpenAI
import json
import pydantic
from dotenv import load_dotenv
from classes.contentClass import Content

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai = OpenAI()

try:
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"Hello"}], max_tokens=5)
    print("✅ OpenAI API loaded in successfully")
except Exception as e:
    print(f"❌ Some error occured: {e}")

