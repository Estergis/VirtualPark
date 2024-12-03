class Park:
    def __init__(self, name: str):
        self.name = name
        self.objects = []  # Список объектов парка

    def add_object(self, park_object):
        self.objects.append(park_object)
        print(f"{park_object.name} added to {self.name}.")

    def describe(self):
        print(f"Park {self.name} contains the following objects:")
        for obj in self.objects:
            obj.describe()

    def start_attractions(self):
        print("Starting all attractions in the park...")
        for obj in self.objects:
            if isinstance(obъект — аттракцион
                obj.start()

    def stop_attractions(self):
        print("Stopping all attractions in the park...")
        for obj in self.objects:
            if isinstaчто объект — аттракцион
                obj.stop()
