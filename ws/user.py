import uuid

from ws.dto import Message, message_broker


class User:
    id: str
    room: str

    def __init__(self):
        self.id = str(uuid.uuid4())

    def create_room(self):
        self.room = str(uuid.uuid4())
        return self.room

    def join_room(self, room: str):
        self.room = room

    def send_msg(self, msg: Message):

    def get_message(self, msg: str):
        dto = message_broker(msg)
        dto.