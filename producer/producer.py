import asyncio
import websockets


async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f'ws://{host}:{port}') as ws:
        await ws.send(message)
        await ws.recv()

while True:
    text = input('user1: ')
    asyncio.run(produce(message=text, host='localhost', port=4000))
