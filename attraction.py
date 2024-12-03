from park_object import ParkObject  # Импортируем родительский класс

class Attraction(ParkObject):
    def __init__(self, name: str, location: str, capacity: int, speed: float):
        super().__init__(name, location)
        self.capacity = capacity
        self.speed = speed

    def start(self) -> str:
        start_message = f"Attraction {self.name} is starting at speed {self.speed}."
        print(start_message)
        return start_message

    def stop(self) -> str:
        stop_message = f"Attraction {self.name} has stopped."
        print(stop_message)
        return stop_message