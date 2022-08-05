class Person():
    """Модель человека"""

    def __init__(self, name, age):
        '''Инициализация атрибутов человека - имя, возраст'''
        self.name = name
        self.age = age
        print('Человек создан')

    def sing(self):
        '''Sing'''
        print(self.name + ' sing')

    def dance(self):
        '''Dance'''
        print(self.name + ' dance')


man = Person('Alex', 20)
woman = Person('Jane', 18)
print(man.name)
man.dance()
man.sing()
woman.sing()