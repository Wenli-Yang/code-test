from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()


class ConnectionManager:

    def __init__(self):
        # active connections save as list
        self.active_connections: List[WebSocket] = []
        # usernames save as dict
        self.usernames: dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.usernames[websocket] = username

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        del self.usernames[websocket]

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"{username}: {data}"
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} has left the chat")