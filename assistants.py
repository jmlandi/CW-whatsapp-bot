from openai import OpenAI
from knowledge import marta_rules
import os

client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))

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
