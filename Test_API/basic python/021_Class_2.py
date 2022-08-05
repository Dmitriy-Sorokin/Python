class Person():
    '''Create people'''

    def __init__(self, name, age, height):
        '''atribut people'''
        self.name = name
        self.age = age
        self.height = height
        self.weight = 80

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



man = Person('Alex', 30, 180)
# man.weight = 110
man.update_weight(300)
man.description_person()
man.get_weight()
