class Annimal:
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):  # NAME - индивидуальное название каждого животного.
        self.name = name

    def eat(self, food):
        self.food = food
        if food == Plant.edible:
            print(self.name, "сьел", food.name)
        else:
            fed = True
        if food != Plant.edible:
            print(self.name, "не стал есть", food.name)
        else:
            alive = False


class Plant:
    edible = False  # съедобность

    def __init__(self, name):  # NAME - индивидуальное название каждого растения.
        self.name = name


class Mammal(Annimal):
    pass


class Predator(Annimal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

