import uuid
from fastapi.websockets import WebSocket

from ws.dto import ChatMessage, Message, message_broker


class User:
    id: str
    room: str
    ws: WebSocket

    def __init__(self, ws: WebSocket):
        self.id = str(uuid.uuid4())
        self.ws = ws

    def create_room(self):
        self.room = str(uuid.uuid4())
        return self.room

    def join_room(self, room: str):
        self.room = room

    def send_msg(self, msg: Message):
        ChatMessage()

    def get_message(self, msg: str):
        dto = message_broker(msg)
        