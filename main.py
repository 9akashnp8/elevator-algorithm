import time
import logging

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
    
    def go_to_floor(self, floor):
        loop_increment = direction = 1
        if floor < self.curr_floor: loop_increment = direction -1
        self.destination_floor = floor
        logger.info(f"currently on: {self.curr_floor}, moving to {self.destination_floor}")

        for i in range(self.curr_floor, self.destination_floor+loop_increment, direction):
            time.sleep(1)
            self.curr_floor = i
            logger.info(f"currently on: {self.curr_floor}")
        
        logger.info("movement complete")

def main():
    elevator = Elevator(1200, 10)
    while True:
        destination_floor = int(input("Input Destination Floor: "))
        elevator.go_to_floor(destination_floor)

if __name__ == '__main__':
    main()

