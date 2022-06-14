import uuid

from fastapi.websockets import WebSocket, WebSocketDisconnect
import json


class SocketInstance:
    ws: WebSocket
    user: str

    def __init__(self, ws: WebSocket):
        self.ws = ws
        self.user = str(uuid.uuid4())

    async def init(self):
        await self.ws.accept()
