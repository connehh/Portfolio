
# C10-1 Creating the class called Monster in order to complete the assignment!
class Monster:

    def __init__(self, name, monster_type):
        self.name = name
        self.monster_type = monster_type

    def set_name(self):
        self.name = input('What is the name of your monster? ')
        return self.name

    def set_monster_type(self):
        self.monster_type = input('What kind of monster are you? ')
        return self.monster_type

    def get_name(self):
        return f'Your name is {self.name}'

    def get_type(self):
        return f'You are a {self.monster_type}'

    def scare(self):
        print(f'The {self.monster_type} is thinking how they should scare you..')
        if self.monster_type == 'Frankenstein':
            print('Fire Bad!')
        elif self.monster_type == 'Werewolf':
            print('Awoooo!')
        elif self.monster_type == 'Dracula':
            print('Bleh!')
        else:
            print('Boo!')
        print('-------')
        print('-------')


monster_instance1 = Monster('default', 'default')
monster_instance2 = Monster('default', 'default')


def monster1():
    monster_instance1.set_name()
    monster_instance1.set_monster_type()

    print(monster_instance1.get_name())
    print(monster_instance1.get_type())
    monster_instance1.scare()


def monster2():
    monster_instance2.set_name()
    monster_instance2.set_monster_type()

    print(monster_instance2.get_name())
    print(monster_instance2.get_type())
    monster_instance2.scare()


monster1()
monster2()
