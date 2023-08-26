import asyncio
import logging
import aioconsole
from queue import Queue

logging.basicConfig(
    level=logging.NOTSET,
    format='%(levelname)s:%(message)s'
)
logger = logging.getLogger()
FLOORS = [i for i in range(10)]

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
    
    async def go_to_floor(self, queue):
        while True:
            if not queue.empty():
                floor = queue.get()
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
    elevator_task = asyncio.create_task(elevator.go_to_floor(queue))
    collector_task = asyncio.create_task(input.collector(queue))
    await asyncio.gather(elevator_task, collector_task)

if __name__ == '__main__':
    asyncio.run(main())
