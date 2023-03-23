import os
import sys


CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)

from chatgpt_response.openai_gateway import OpenAiGateway


class PilotService:

    def __init__(self, openai_gateway=OpenAiGateway()):
        self.openai_gateway = openai_gateway

    def ask(self, query):
        requestData = ('{'
                       '"model": "gpt-3.5-turbo",'
                       '"messages": [{"role": "user", "content": "' + query + '"}],'
                       '"temperature": 0.7'
                       '}'
                       )

        response = self.openai_gateway.completion(requestData)

        return response
