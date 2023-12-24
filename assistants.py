from openai import OpenAI
from knowledge import bruno_rules
import os

client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))

class Bruno():

    def response(prompt, rules = bruno_rules):
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
            max_tokens = 300
        )

        return completion.choices[0].message.content