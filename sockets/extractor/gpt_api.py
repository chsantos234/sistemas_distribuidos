from openai import OpenAI
from env import env

class Gptapi():

    def __init__(self):
        self.api_key = f"{env('GPT-KEY')}"
        self.client = OpenAI(api_key=self.api_key)
        self.assistant = self.client.beta.assistants.retrieve("asst_4uAa9082Z9eYTNiYkGwyF67f")
        self.thread = self.client.beta.threads.create()
        self.model = self.assistant.model
        self.t_id = self.thread.id
        self.ass_id =  self.assistant.id

    def send_message(self,content):

        self.client.beta.threads.messages.create(
            thread_id=self.t_id,
            role="user",
            content=content
        )

        run = self.client.beta.threads.runs.create(
            thread_id=self.t_id,
            assistant_id=self.ass_id
        )

        while True:

            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.t_id,
                run_id=run.id
            )

            if run.status != "in_progress":
                break 

        messages = self.client.beta.threads.messages.list(thread_id=self.t_id)

        try:
            return messages.data[0].content[0].text.value
        except:
            return "Algum error ocorreu veyr"