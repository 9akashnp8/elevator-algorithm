import json
import asyncio
import redis
from fastapi import WebSocket

from models import FloorRequest
from utils import initial_req_msg

class Queue():
    """simeple wrapper around Redis,
    uses Redis Lists to implement
    a "Queue"
    """
    connection = redis.Redis()

    @property
    def has_unprocessed_requests(self):
        return self.connection.llen(f"temp_{self.name}")

    def __init__(self, name: str) -> None:
        self.name = name

    def len(self):
        return self.connection.llen(self.name)

    def enqueue(self, request: dict):
        value = json.dumps(request)
        self.connection.lpush(self.name, value)

    def dequeue(self) -> dict:
        if self.connection.llen(self.name):
            if self.has_unprocessed_requests:
                return json.loads(self.connection.rpop(f"temp_{self.name}"))
            return json.loads(self.connection.rpoplpush(self.name, f"temp_{self.name}"))
    

class Elevator():
    max_weight: int
    max_heads: int
    is_running: bool
    curr_floor: int = 0
    destination_floor: int
    websocket: WebSocket = None

    def __init__(
        self,
        max_weight: int,
        max_heads: int
    ) -> None:
        self.max_weight = max_weight
        self.max_heads = max_heads

    def link_websocket(self, websocket: WebSocket):
        self.websocket = websocket

    async def go_to_floor(self, req_from, destination_floor):
        if not self.websocket: return
        direction = step = 1
        await self.websocket.send_json({"action": "initiated", "current": self.curr_floor})

        if req_from != self.curr_floor:
            for i in range(self.curr_floor+1, req_from+1):
                await asyncio.sleep(1)
                self.curr_floor = i
                await self.websocket.send_json({"action": "moving", "current": i})

        if destination_floor < self.curr_floor: direction = step = -1
        for j in range(self.curr_floor + step, destination_floor + step, direction):
            await asyncio.sleep(1)
            self.curr_floor = j
            await self.websocket.send_json({"action": "moving", "current": j})

        await self.websocket.send_json({"action": "complete", "current": self.curr_floor})

    async def run(self, queue: Queue):
        while True:
            floor_request = queue.dequeue()
            
            if floor_request:
                destination_level = floor_request.get('destination_level')
                req_from = floor_request.get('current_level')
                await self.go_to_floor(req_from, destination_level)
                queue.dequeue_temp()

            await asyncio.sleep(0.5)
