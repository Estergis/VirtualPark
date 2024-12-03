from park_object import ParkObject

# Базовый класс для всех заведений
class FoodEstablishment(ParkObject):
    def __init__(self, name: str, location: str, menu: list):
        super().__init__(name, location)
        self.menu = menu

    def serveSpeciality(self) -> str:
        serve_message = f"Serving the special dessert from {self.name}."
        print(serve_message)
        return serve_message


# Класс для заведений с шоколадными десертами
class ChocolateDessertShop(FoodEstablishment):
    def __init__(self, name: str, location: str):
        desserts = ["Chocolate Cake", "Chocolate Mousse"]
        super().__init__(name, location, desserts)

    def serveSpeciality(self) -> str:
        serve_message = f"Serving the chocolate dessert specialty at {self.name}: {self.menu[0]} and {self.menu[1]}."
        print(serve_message)
        return serve_message


# Класс для заведений с оливковыми десертами
class OliveDessertShop(FoodEstablishment):
    def __init__(self, name: str, location: str):
        desserts = ["Olive Cake", "Olive Mousse"]
        super().__init__(name, location, desserts)

    def serveSpeciality(self) -> str:
        serve_message = f"Serving the olive dessert specialty at {self.name}: {self.menu[0]} and {self.menu[1]}."
        print(serve_message)
        return serve_message


# Класс для кафе с меню
class Cafe(FoodEstablishment):
    def __init__(self, name: str, location: str):
        menu = ["First Course", "Second Course", "Third Course"]
        super().__init__(name, location, menu)

    def serveSpeciality(self) -> str:
        serve_message = f"Serving the full meal at {self.name}: {', '.join(self.menu)}."
        print(serve_message)
        return serve_message
