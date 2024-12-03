from park_object import ParkObject

class Shop(ParkObject):
    def __init__(self, name: str, location: str, items: list):
        super().__init__(name, location)
        self.items = items

    def listItems(self) -> str:
        items_list = ", ".join(self.items)
        list_message = f"Items available in {self.name}: {items_list}."
        print(list_message)
        return list_message

    def buyItem(self, itemName: str) -> str:
        if itemName in self.items:
            purchase_message = f"Item {itemName} has been purchased from {self.name}."
        else:
            purchase_message = f"Item {itemName} is not available in {self.name}."
        print(purchase_message)
        reten purchase_message
