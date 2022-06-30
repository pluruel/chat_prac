from abc import abstractmethod, ABC
import json
from fastapi.websockets import WebSocket


class DTO:
    def __init__(self):
        raw = dict()


class Message(DTO, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_value(data, key):
        pass


class JsonMessage(Message, ABC):
    type: str

    def __init__(self, *args, **kwargs):
        super(JsonMessage, self).__init__(*args, **kwargs)

    def get_value(data, key):
        assert type(data) == dict and type(key) == str, "wrong data"
        return data.get(key)

    @abstractmethod
    def load(self, raw: str):
        pass

    @abstractmethod
    def pack(self):
        pass


class SystemMessage(JsonMessage):
    code: str
    attr: dict
    time: int

    def __init__(self, **kwargs):
        super(SystemMessage, self).__init__(**kwargs)

    def load(self):
        self.code = self.raw.get("code")
        self.attr = self.raw.get("attr")
        self.time = self.raw.get("time")

    def pack(
        self,
    ):
        return {
            "type": self.type,
            "code": self.code,
            "attr": self.attr,
            "time": self.time,
        }


class ChatMessage(Message):
    chat_data: str
    time: int

    def __init__(self, **kwargs):
        super(ChatMessage, self).__init__(**kwargs)

    def load(self):
        self.chat_data = self.raw.get("chat_data")
        self.time = self.raw.get("time")

    def pack(self, msg: str):
        return {"chat_data": msg, "time": self.time}


def message_broker(msg: str) -> JsonMessage:
    msg_dict = json.loads(msg)
    msg_type = msg_dict.get("type")
    assert msg_type in ["system", "chat"], "This message may not proper."

    msg_cls_dict = {"system": SystemMessage, "chat": ChatMessage}
    return msg_cls_dict[msg_type](msg_dict)
