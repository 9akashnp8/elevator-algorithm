import asyncio

FLOORS = [i for i in range(10)]

class Elevator():
    max_weight: int
    max_heads: int
    is_running: bool
    curr_floor: int = 10
    destination_floor: int = 20

    def __init__(
        self,
        max_weight: int,
        max_heads: int,
        is_running: bool = False
    ) -> None:
        self.max_weight = max_weight
        self.max_heads = max_heads
        self.is_running = is_running
    
    async def go_to_floor(self, floor):
        self.destination_floor = floor
        print(f"Moving to floor: {self.destination_floor}")
        for i in range(self.curr_floor, self.destination_floor):
            await asyncio.sleep(5)
            self.curr_floor = i
            print("Currently on floor: ", self.curr_floor)
        print(f"Moving complete, current floor: {self.curr_floor}")

    async def go_up(self):
        asyncio.create_task(self.go_to_floor(max(FLOORS)))
    
    async def go_down(self):
        asyncio.create_task(self.go_to_floor(min(FLOORS)))
    
    def run(self):
        print("RUNNING")
        asyncio.run(self.go_up())
        print("COMPLETE")

