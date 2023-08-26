import asyncio
import logging
import aioconsole
from queue import Queue

from models import FloorRequest
from utils import initial_req_msg

logging.basicConfig(
    level=logging.NOTSET,
    format='%(levelname)s:%(message)s'
)
logger = logging.getLogger()

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
    
    async def run(self, queue: Queue[FloorRequest]):
        while True:
            if not queue.empty():
                curr_item = queue.get()
                destination_level = curr_item.destination_level
                req_from = curr_item.current_level
                await self.go_to_floor(req_from, destination_level)
            await asyncio.sleep(0.5)

class InputCollector():

    async def collector(self, queue):
        while True:
            user_input = await aioconsole.ainput("Enter a request: \n")
            queue.put(user_input)
            await asyncio.sleep(0.2)

async def main():
    elevator = Elevator(1200, 10)
    input = InputCollector()
    queue = Queue()
    elevator_task = asyncio.create_task(elevator.run(queue))
    collector_task = asyncio.create_task(input.collector(queue))
    await asyncio.gather(elevator_task, collector_task)

if __name__ == '__main__':
    asyncio.run(main())
