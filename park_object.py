class ParkObject:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def describe(self) -> str:
        # Описание объекта парка
        description = f"{self.name} located at {self.location}"
        print(description)  
        return description

    def start(self) -> str:
        # Запуск аттракциона
        start_message = f"Attraction {self.name} is starting."
        print(start_message)  
        return start_message

    def stop(self) -> str:
        # Остановка аттракциона
        stop_message = f"Attraction {self.name} has stopped."
        print(stop_message)  
        return stop_message
