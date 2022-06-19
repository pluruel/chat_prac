from abc import abstractmethod
import json


class DTO:
    raw: dict

    def __init__(self, msg: str):
        raw = json.loads(msg)


class Message(DTO):
    type: str

    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)
        self.type = self.raw.get('type')
        assert type(self.type) is str


    @abstractmethod
    def run(self):
        pass


class SystemMessage(Message):
    code: str

    def __init__(self):
        super(SystemMessage, self).__init__()
        self.code = self.raw.get('code')

    def run(self, socket: W):
        getattr(self, self.code)()
        

class ChatMessage(Message):
    chat_data: str

    def __init__(self):
        super(ChatMessage, self).__init__()
        self.chat_data = self.raw.get('chat_data')

    def run(self):
        