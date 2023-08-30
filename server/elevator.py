import json
import asyncio
import redis

from models import FloorRequest
from utils import initial_req_msg

class Queue():
    """simeple wrapper around Redis,
    uses Redis Lists to implement
    a "Queue"
    """
    connection = redis.Redis()

    def __init__(self, name: str) -> None:
        self.name = name

    def len(self):
        return self.connection.llen(self.name)

    def enqueue(self, request: dict):
        value = json.dumps(request)
        self.connection.lpush(self.name, value)

    def dequeue(self) -> dict:
        return json.loads(self.connection.rpop(self.name))

class Elevator():
    max_weight: int
    max_heads: int
    is_running: bool
    curr_floor: int = 0
    destination_floor: int

    def __init__(
        self,
        max_weight: int,
        max_heads: int
    ) -> None:
        self.max_weight = max_weight
        self.max_heads = max_heads

    async def go_to_floor(self, req_from, destination_floor):
        print(initial_req_msg(destination_floor, req_from, self.curr_floor))
        if self.curr_floor != req_from:
            print(f"Now going to: {req_from}")
            await asyncio.sleep(5)
            self.curr_floor = req_from
            print(f"Reached {req_from}, going to {destination_floor}")
        await asyncio.sleep(5)
        self.curr_floor = destination_floor
        print("Reached destination", destination_floor)
    
    async def run(self, queue: Queue):
        while True:
            if queue.len():
                curr_item = queue.dequeue()
                destination_level = curr_item.get('destination_level')
                req_from = curr_item.get('current_level')
                await self.go_to_floor(req_from, destination_level)
            await asyncio.sleep(0.5)
