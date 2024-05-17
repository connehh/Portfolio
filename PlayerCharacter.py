import random

class Player:

    def __init__(self, health, power, defense):
        self.health = health
        self.power = power
        self.defense = defense


    def levelup(self):
        self.power += 1
        self.defense += 1
        print('LEVEL UP!!')
        return f'Your attack power has increased to {self.power} and your defense has increased to {self.defense}!'


    def attack(self):
        multiplier = random.randint(1, 2)
        mainattack = self.power * multiplier
        return mainattack


    def take_hit(self, damage):
        damagetaken = damage - self.defense
        self.health -= damagetaken
        return f'Your armour was only able to shield {self.defense} point(s) of damage, ' \
               f'your health is now: {self.health}'


    # def knockout(self, health):
        # if health == 0:

# character = Player(10, 1, 1)

# print(character.take_hit(2))
