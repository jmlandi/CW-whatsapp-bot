from openai import OpenAI
from knowledge import bruno_rules
import os

client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))
bruno_id = "asst_VvGXR2BdIltIKSoEuJhLusP3"

# creating file and assistant on OpenAi API
def gpt_init():
    file_list, file_count = client.files.list(), 0
    for file in file_list.data:
        if file.filename == "infinitepay":
            file_count +=1

    if file_count == 0:
        knowledge_file = client.files.create(
            file = open("knowledge/infinitepay.txt", "rb"),
            purpose = "assistants"
        )
        
    assistant_list, assistant_count = client.beta.assistants.list(), 0
    for assistant in assistant_list.data:
        if assistant.name == "Bruno":
            assistant_count += 1

    if assistant_count == 0:
        client.beta.assistants.create(
            name = "Bruno",
            instructions = "Seu nome Bruno. Você é uma agente de suporte que atenderá apenas clientes da empresa InfinitePay, sua função é tirar dúvidas simples sobre produtos da InfinitePay dentro do WhatsApp. Você trata seus clientes sempre com linguagem neutra, com linguajar acolhedor e bem-humorado. Ao final de suas mensagens, pergunte se pode ajudar em algo mais. Se não houver informações suficientes ou o cliente precisar de suporte, oriente o cliente entrar em contato nos canais de suporte",
            tools = [{"type": "retrieval"}],
            model = "gpt-3.5-turbo-1106",
            file_ids = [knowledge_file.id]
        )

# Setting functions to run threads and responses
class Bruno():

    def thread_init():
        thread = client.beta.threads.create()
        return thread
    
    def thread_message(thread, prompt):
        message = client.beta.threads.messages.create(
            thread_id = thread.id,
            role = "user",
            content = prompt
        )
        return message
    
    def thread_run(thread, instructions, assistant_id = bruno_id):
        run = client.beta.threads.runs.create(
            thread_id = thread.id,
            instructions = instructions,
            assistant_id = assistant_id
        )
        return run
    
    def thread_retrieve_run(thread, run):
        retrieve = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )
        return retrieve

    def thread_messages_list(thread):
        messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )
        messages_list = []
        for message in reversed(messages.data):
            messages_list.append(f"{message.role}: {message.content[0].text.value}")
        return messages_list
    
    def thread_assitant_reponse(thread):
        response = client.beta.threads.messages.list(
            thread_id = thread.id,
            limit = 1
        )
        return response.data.content[0].text.value


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
            max_tokens = 72
        )

        return completion.choices[0].message.content