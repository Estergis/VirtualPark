from park import Park
from attraction import Attraction
from food_establishment import FoodEstablishment
from shop import Shop
from theater import Theater

# Создание объекта парка
virtual_park = Park()

# Создание аттракционов
carousel = Attraction(name="Carousel", location="Area 1", capacity=20, speed=5)
roller_coaster = Attraction(name="Roller Coaster", location="Area 2", capacity=15, speed=10)

# Добавление аттракционов в парк
virtual_park.addObject(carousel)
virtual_park.addObject(roller_coaster)

# Создание заведений с десертами
dessert_shop1 = FoodEstablishment(name="Chocolate Delights", location="Food Area 1", menu=["Chocolate Cake", "Chocolate Mousse"], specialty="Chocolate")
dessert_shop2 = FoodEstablishment(name="Olive Bakery", location="Food Area 2", menu=["Olive Cake", "Olive Mousse"], specialty="Olives")

# Добавление заведений в парк
virtual_park.addObject(dessert_shop1)
virtual_park.addObject(dessert_shop2)

# Создание магазина
souvenir_shop = Shop(name="Souvenir Shop", location="Main Street", items=["T-shirts", "Mugs", "Postcards"])

# Добавление магазина в парк
virtual_park.addObject(souvenir_shop)

# Создание театральной площадки
theater = Theater(name="Virtual Theater", location="Entertainment Zone", showSchedule=["2 PM - Magic Show", "4 PM - Puppet Show"])

# Добавление театра в парк
virtual_park.addObject(theater)

# Запуск аттракционов
carousel.start()
roller_coaster.start()

# Остановка аттракционов
carousel.stop()
roller_coaster.stop()

# Печать списка объектов парка
print(virtual_park.listObjects())