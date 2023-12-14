from openai import OpenAI
from dotenv import load_dotenv
from knowledge import marta_rules
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key = openai_api_key)

class Marta():
    
    def response(prompt, rules = marta_rules):
        completion = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {
                    'role': 'system',
                    'content': rules
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            max_tokens = 256
        )

        return completion.choices[0].message.content
    
    def thread():
        'this will be a Marta Thread Function'
