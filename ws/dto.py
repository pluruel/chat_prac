from abc import abstractmethod, ABC
import json
from fastapi.websockets import WebSocket


class DTO:
    raw: dict

    def __init__(self, msg: dict):
        raw = dict


class Message(DTO):
    type: str

    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)
        self.type = self.raw.get('type')
        assert type(self.type) is str
        self.parse()

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def pack(self):
        pass


class SystemMessage(Message, ABC):
    code: str
    attr: dict
    time: int

    def __init__(self, **kwargs):
        super(SystemMessage, self).__init__(**kwargs)

    def parse(self):
        self.code = self.raw.get('code')
        self.attr = self.raw.get('attr')
        self.time = self.raw.get('time')

    def pack(self):
        return {
            'code': self.code,
            'attr': self.attr,
            'time': self.time
        }


class ChatMessage(Message, ABC):
    chat_data: str
    time: int

    def __init__(self, **kwargs):
        super(ChatMessage, self).__init__(**kwargs)

    def parse(self):
        self.chat_data = self.raw.get('chat_data')
        self.time = self.raw.get('time')

    def pack(self):
        return {
            'chat_data': self.code,
            'time': self.time
        }


def message_broker(msg: str) -> Message:
    msg_dict = json.loads(msg)
    msg_type = msg_dict.get('type')
    assert msg_type in ['system', 'chat'], 'This message may not proper.'

    msg_cls_dict = {
        'system': SystemMessage,
        'chat': ChatMessage
    }
    return msg_cls_dict[msg_type](msg_dict)
