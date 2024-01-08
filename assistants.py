from openai import OpenAI
from knowledge import bruno_rules
import os

client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))
bruno_id = "asst_bPcCzTiOxUNvpMUR7LtAmgQ9"

# creating assistant on OpenAi API
def gpt_init():

    assistant_list, assistant_count = client.beta.assistants.list(), 0
    for assistant in assistant_list.data:
        if assistant.name == "Bruno":
            assistant_count += 1

    if assistant_count == 0:
        client.beta.assistants.create(
            name = "Bruno",
            instructions = bruno_rules,
            model = "gpt-3.5-turbo-1106"
        )

# Setting functions to run threads and responses
class Bruno():

    def thread_init():
        thread = client.beta.threads.create()
        return thread
    
    def thread_message(thread_id, prompt):
        message = client.beta.threads.messages.create(
            thread_id = thread_id,
            role = "user",
            content = prompt
        )
        return message
    
    def thread_run(thread_id, instructions, assistant_id = bruno_id):
        run = client.beta.threads.runs.create(
            thread_id = thread_id,
            instructions = instructions,
            assistant_id = assistant_id
        )
        return run
    
    def thread_retrieve_run(thread_id, run):
        retrieve = client.beta.threads.runs.retrieve(
            thread_id = thread_id,
            run_id = run.id
        )
        return retrieve

    def thread_messages_list(thread_id):
        messages = client.beta.threads.messages.list(
            thread_id = thread_id
        )
        messages_list = []
        for message in reversed(messages.data):
            messages_list.append(f"{message.role}: {message.content[0].text.value}")
        return messages_list
    
    def thread_assitant_reponse(thread_id):
        response = client.beta.threads.messages.list(
            thread_id = thread_id
        )
        return response.data[0].content[0].text.value

    def bruno_completion(prompt):  
        completion = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {
                    'role': 'system',
                    'content': bruno_rules
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            max_tokens = 499
        )
        return completion.choices[0].message.content
    