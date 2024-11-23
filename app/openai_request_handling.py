import os
from openai import OpenAI
from pyexpat.errors import messages


class OpenaiRequestHandling:
    def __init__(self, model):
        self.model = model
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

    # messageのリストを作成
    @staticmethod
    def create_request_message(system_prompt, user_prompt):
        api_messages = []
        if system_prompt is not None:
            api_messages.append(system_prompt)
        if user_prompt is not None:
            api_messages.extend(user_prompt)
        return api_messages

    # apiを呼び出して，responseを取得
    def get_response(self, temperature, response_format, system_prompt, user_prompt):
        return self.client.beta.chat.completions.parse(
            model=self.model,
            messages=OpenaiRequestHandling.create_request_message(system_prompt, user_prompt),
            temperature=temperature,
            response_format=response_format,
        )