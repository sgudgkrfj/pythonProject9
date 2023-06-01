
class FoodItem:
    def __init__(self, name, description, price):
        super().__init__()
        self.name = name
        self.description = description
        self.price = price

class Menu:
    def __init__(self):
        super().__init__()
        self.dishes = []

    def add_food(self, food):
        self.dishes.append(food)

    def remove_food(self, food):
        removed_food = next(filter(lambda j: j.name == food.name and
                                               j.description == food.description and
                                               j.price == food.price, self.dishes), None)

        if removed_food is not None:
            self.dishes.remove(removed_food)
        else:
            return f"Страва {removed_food} відсутня в меню"

class Order:
    def __init__(self):
        super().__init__()
        self.list_of_dishes = []

    def add_to_order(self, food):
        i = 0
        self.list_of_dishes.append(food)
        for food in self.list_of_dishes:
            i += food.price
        print(f"Вартість страв: {i}")
salad = FoodItem("Салат", "Складається з я'єць, зелені та заправок", 150)
borsch = FoodItem("Борщ", "Склад борщу", 200)
dumplings = FoodItem("Вареники", "Склад вареників", 100)

menu = Menu()


menu.add_food(salad)
menu.add_food(borsch)
menu.add_food(dumplings)

order = Order()

order.add_to_order(salad)
order.add_to_order(borsch)
order.add_to_order(dumplings)






