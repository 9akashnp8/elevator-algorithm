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
        return json.loads(self.connection.rpoplpush(self.name, f"temp_{self.name}"))

    def dequeue_temp(self) -> dict:
        return json.loads(self.connection.rpop(f"temp_{self.name}"))

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

    def prepare_floor_request(self, queue: Queue):
        floor_request = {}
        if queue.has_unprocessed_requests:
            floor_request = queue.dequeue_temp()
        elif queue.len():
            floor_request = queue.dequeue()
        return floor_request

    async def go_to_floor(self, req_from, destination_floor):
        await self.websocket.send_text(
            initial_req_msg(destination_floor, req_from, self.curr_floor))
        if self.curr_floor != req_from:
            await self.websocket.send_text(f"Now going to: {req_from}")
            await asyncio.sleep(5)
            self.curr_floor = req_from
            await self.websocket.send_text(f"Reached {req_from}, going to {destination_floor}")
        await asyncio.sleep(5)
        self.curr_floor = destination_floor
        await self.websocket.send_text(f"Reached destination: {destination_floor}")
    
    async def run(self, queue: Queue):
        while True:
            floor_request = self.prepare_floor_request(queue)
            
            if floor_request:
                destination_level = floor_request.get('destination_level')
                req_from = floor_request.get('current_level')
                await self.go_to_floor(req_from, destination_level)
                queue.dequeue_temp()

            await asyncio.sleep(0.5)
