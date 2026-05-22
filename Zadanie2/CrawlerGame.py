class Dungeon:
    def __init__(self):
        self.rooms = []

    def generate_rooms(self):
        pass

class Room:
    def __init__(self, north_room, south_room, east_room, west_room):
        self.north_room = north_room
        self.south_room = south_room
        self.east_room = east_room
        self.west_room = west_room

class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

class Hero:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg
        self.inventory = []

    def attack(self, monster):
        monster.hp -= self.dmg

class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price