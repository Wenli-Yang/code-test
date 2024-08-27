import asyncio
import websockets

async def chat():
    uri = "ws://localhost:8000/ws/your_username"
    async with websockets.connect(uri) as websocket:
        print("Connected to the chat server")

        async def send_message():
            while True:
                message = input("You: ")
                await websocket.send(message)

        async def receive_message():
            while True:
                message = await websocket.recv()
                print(f"\n{message}")

        await asyncio.gather(send_message(), receive_message())

if __name__ == "__main__":
    asyncio.run(chat())