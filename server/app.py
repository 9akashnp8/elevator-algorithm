import json
import asyncio
from typing import Any
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from models import FloorRequest, RequestID
from elevator import Elevator, Queue

app = FastAPI()
elevator = Elevator(1200, 20)
queue: Queue = Queue("floor_requests")
origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Response(BaseModel):
    status: str
    message: str
    body: Any = None

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(elevator.run(queue))

@app.get("/")
def get_root() -> Response:
    return Response(
        status="success",
        message="Root Endpoint"
    )

@app.post("/floor")
def go_to_floor(body: FloorRequest):
    queue.enqueue(body.model_dump())
    return Response(
        status="success",
        message="request queued",
        body=RequestID(request_id="123")
    )

@app.get("/queue")
def get_current_queue():
    return Response(
        status="success",
        message="",
        body=[item for item in queue.queue]
    )

@app.websocket("/ws")
async def elevator_websocket(websocket: WebSocket):
    elevator.link_websocket(websocket)
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data:
            queue.enqueue(json.loads(data))
        else:
            await websocket.send_text("Empty Request")
