from park_object import ParkObject

class Theater(ParkObject):
    def __init__(self, name: str, location: str, showSchedule: list):
        super().__init__(name, location)
        self.showSchedule = showSchedule

    def startShow(self, showName: str) -> str:
        if showName in self.showSchedule:
            start_message = f"Starting the show {showName} at {self.name}."
        else:
            start_message = f"The show {showName} is not scheduled at {self.name}."
        print(start_message)
        return start_message