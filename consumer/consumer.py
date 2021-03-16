import asyncio
import logging
import websockets
from websockets import WebSocketClientProtocol

logging.basicConfig(level=logging.INFO)


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    async for message in websocket:
        log_message(message)


async def consume(hostname: str, port: int) -> None:
    websocket_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)


def log_message(message: str) -> None:
    logging.info(f"Message: {message}")


async def produce(host: str, port: int) -> None:
    while True:
        text = input('user1: ')
        async with websockets.connect(f'ws://{host}:{port}') as ws:
            await ws.send(text)
            await ws.recv()


if __name__ == '__main__':
    asyncio.run(produce(host='localhost', port=4000))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume(hostname='localhost', port=4000))
    loop.run_forever()
