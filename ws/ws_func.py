import asyncio
import json

from aioredis import Redis
from fastapi.websockets import WebSocket, WebSocketDisconnect

import async_timeout

def handle_system_msg(ws: WebSocket, msg: str):
    funcs = {
        "handshake":
    }

def handle_chat_msg(ws: WebSocket, msg: str):
    chat = json.loads(meg)

def handle_msg(ws: WebSocket, msg: str):
    message = json.loads(msg)
    type =


async def consumer_handler(ws: WebSocket, r: Redis, logger):
    try:
        while True:
            message = await ws.receive_text()
            if message:
                d = json.loads(message)
                print(d)
                if d['data'] == 'EXIT':
                    await r.publish("channel:1", 'goodbye')
                    break;
                await r.publish("channel:1", d['data'])

    except WebSocketDisconnect as exc:
        # TODO this needs handling better
        await r.publish("channel:1", 'goodbye')
        logger.error(exc)

async def producer_handler(r: Redis, ws: WebSocket, logger):
    psub = r.pubsub()
    await psub.subscribe("channel:1")
    try:
        while True:
            async with async_timeout.timeout(1):
                message = await psub.get_message(ignore_subscribe_messages=True)
                if message is not None:
                    await ws.send_text(message['data'])

                await asyncio.sleep(0.01)
    except Exception as exc:
        logger.error(exc)
