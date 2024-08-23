import asyncio
from fastapi import WebSocket

async def chat():
    uri = "ws://localhost:8000/ws/your_username"
    websocket = WebSocket(uri)
    await websocket.connect()
    print("Connected to the chat server")

    async def send_message():
        while True:
            message = input("You: ")
            await websocket.send_text(message)

    async def receive_message():
        while True:
            message = await websocket.receive_text()
            print(f"\n{message}")

    await asyncio.gather(send_message(), receive_message())

if __name__ == "__main__":
    asyncio.run(chat())