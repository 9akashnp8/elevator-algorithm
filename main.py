class Elevator():
    max_weight: int
    max_heads: int
    is_running: bool

    def __init__(
        self,
        max_weight: int,
        max_heads: int,
        is_running: bool = False
    ) -> None:
        self.max_weight = max_weight
        self.max_heads = max_heads
        self.is_running = is_running

class Main():

    def __init__(self):
        self.elevator_instance = Elevator(1200, 12)
    
    def run(self, mock: bool):
        setattr(self.elevator_instance, 'is_running', True)
