import random


class Pokemon:
    def __init__(self, name, type1, type2, attack, defense, spattack, spdef, spd):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.attack = attack
        self.defense = defense
        self.spattack = spattack
        self.spdef = spdef
        self.spd = spd

    def toString(self):
        return str(self.name)
