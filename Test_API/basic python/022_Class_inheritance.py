class Person():
    '''Create people'''

    def __init__(self, name, age, height):
        '''atribut people'''
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        '''Getting a description of the person'''
        description = self.name + ', hes ' + str(self.age) + ", hes height " + str(self.height) + " hes weight " + str(
            self.weight)
        print('Name news person : ' + description)

    def get_weight(self):
        '''get weight'''
        print("weight person :" + str(self.weight))

    def update_weight(self, kg):
        '''update weight person'''
        self.weight = kg

class Warrior(Person):
    '''Create class warrior'''

    def __init__(self, name, age, height):
        '''Initialize class attributes'''
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        '''get rage'''
        print('Get rage : ' + str(self.rage))

    def description_person(self):
        '''Переопределение метода родителя'''
        description = self.name + ', hes ' + str(self.age) + ' rage ' + str(self.rage)
        # print('Name news person : ' + description)
        return description
#
# warrior = Warrior('Wigi', 30, 200)
# # warrior.update_weight(150)
# # warrior.description_person()
# # warrior.get_rage()
# print('Name : ' + warrior.description_person())



# man = Person('Alex', 30, 180)
# # man.weight = 110
# man.update_weight(300)
# man.description_person()
# man.get_weight()