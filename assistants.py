from openai import OpenAI
from knowledge import bruno_rules
import os

client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))

'''
knowledge_file = client.files.create(
    file = open("knowledge/bruno_knowledge.csv", "rb"),
    purpose = "assistants"
)
'''

assistant = client.beta.assistants.create(
    name = "Bruno",
    instructions = "Seu nome Bruno. Você é uma agente de suporte que atenderá apenas clientes da empresa InfinitePay. Você trata seus clientes sempre com linguagem neutra, com linguajar acolhedor e bem-humorado. Quebre parágrafos com '\n' para facilitar na visualisação do texto e ao final de suas mensagens pergunte se pode ajudar em algo mais. Para seu atendimento, utilize os conteúdos do site https://ajuda.infinitepay.io/pt-BR/ se não houver informações suficientes ou o cliente precisar de suporte, mande as informações de atendimento com o time especializado, que se encontra no site https://ajuda.infinitepay.io/pt-BR/articles/3406982-quais-sao-os-canais-de-atendimento-da-infinitepay, e-mail ajuda@infinitepay.io ou chat do aplicativo no celular ou computador. De forma educada, recuse atender quaisquer assuntos que não sejam relacionados a empresa InfinitePay.",
    tools = [{"type": "retrieval"}],
    model = "gpt-3.5-turbo-1106",
    file_ids = "file-Sgb2gs4Hqp4fji9pgQ4WbOzW"
)

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
    
    def thread_run(thread, assistant = assistant):
        run = client.beta.threads.runs.create(
            thread_id = thread.id,
            assistant_id = assistant.id
        )
        return run
    
    def thread_response(thread, run):
        client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )

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