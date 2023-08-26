import asyncio
import logging
import aioconsole
from queue import Queue

from models import FloorRequest

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
    
    async def run(self, queue: Queue[FloorRequest]):
        while True:
            if not queue.empty():
                floor = queue.get().level
                print(f"Going to floor: {floor}")
                await asyncio.sleep(5)
                print(f"Movement complete to: {floor}")
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
