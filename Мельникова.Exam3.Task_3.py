class Tomato:

    states = {1: "семечко", 2:"росток", 3:"зеленый", 4:"красный"}

    def __init__(self,index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 4:
            self._state += 1
        print(f'помидор {self._index} - {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 4:
            return True
        else:
            return False

class TomatoBush:

    def __init__(self, amount):
        self.tomatoes =[Tomato(i) for i in range(1,amount)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            return i.is_ripe()

    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Помидоры созрели! Садовник собрал урожай!')
        else:
            print('Помидоры еще не созрели!')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству: из семечка вырастает росток,'
              '\nесли росток поливать и ухаживать за ним, появляются зеленые плоды,'
              '\nпродолжайте ухаживать за ростком и вы сможете собрать красные плоды')

Gardener.knowledge_base()
tomatoes_bushes = TomatoBush(4)
object_gardener = Gardener('nathalia', tomatoes_bushes)
object_gardener.work()
object_gardener.harvest()
object_gardener.work()
object_gardener.harvest()
object_gardener.work()
object_gardener.harvest()
object_gardener.work()
object_gardener.harvest()