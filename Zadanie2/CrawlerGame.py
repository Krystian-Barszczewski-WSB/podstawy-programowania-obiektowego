#Gra Dungeon crawler (podziemia) – klasy Hero, Monster, Room, Item, Dungeon;
# przemieszczanie się między pomieszczeniami, walka, zbieranie skarbów.
import random

class Dungeon:
    def __init__(self, max_rooms = 10):
        self.rooms = {(0, 0): Room(0, 0)}

        self.rooms[(0, 0)].generate_rooms(self.rooms, max_rooms)

        while len(self.rooms) < 5:
            print(self.rooms.keys())
            print(len(self.rooms))
            self.rooms.clear()

            self.rooms = {(0, 0): Room(0, 0)}

            self.rooms[(0, 0)].generate_rooms(self.rooms, max_rooms)

        print(self.rooms.keys())
        print(len(self.rooms))

    def generate_map(self):
        xs = [pos[0] for pos in self.rooms]
        ys = [pos[1] for pos in self.rooms]

        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        for y in range(max_y, min_y - 1, -1):
            for x in range(min_x, max_x + 1):
                if (x, y) in self.rooms:
                    if self.rooms[(x, y)].monsters:
                        print("▲", end=" ")
                    elif (x, y) == (0,0):
                        print("◯", end=" ")
                    else:
                        print("■", end=" ")
                else:
                    print("░", end=" ")
            print()


class Room:
    def __init__(self, x, y):
        self.loot = []
        self.monsters = []
        self.x = x
        self.y = y
        #self.neighboring_rooms = neighboring_rooms # 0-north, 1-south, 2-east, 3-west
        #self.generate()

    def generate(self):
        if random.random() < 0.3:
            self.loot = Item("HP Potion", "Heals the users wounds")
        if random.random() < 0.6:
            self.monsters.append(Goblin())


    def generate_rooms(self, rooms, max_rooms):
        if len(rooms) >= max_rooms:
            return

        for pos in [(-1,0), (0,1), (1,0), (0,-1)]:
            new_pos = (self.x + pos[0], self.y + pos[1])
            if new_pos in rooms:
                continue

            if random.random() < 0.45 and len(rooms) < max_rooms:
                rooms[new_pos] = Room(new_pos[0], new_pos[1])
                rooms[new_pos].generate()
                rooms[new_pos].generate_rooms(rooms, max_rooms)


class Monster:
    def __init__(self, name, hp, dmg, gold_drop):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.gold_drop = gold_drop

    def attack(self, hero):
        hero.hp -= self.dmg

    def use_skill(self, hero):
        pass

class Goblin(Monster):
    def __init__(self):
        super().__init__(
            name="Goblin",
            hp=15,
            dmg=5,
            gold_drop=10
        )

    def use_skill(self, hero):
        how_much = random.randint(1, 10)
        print(f"Goblin steals {how_much} gold")
        hero.gold -= how_much


class Hero:
    def __init__(self, hp, dmg, start_room):
        self._hp = hp
        self.dmg = dmg
        self.inventory = []
        self._gold = 0
        self.current_room = start_room

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = value

        if self._gold <= 0:
            self._gold = 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        print("HP", self._hp)

        if self._hp <= 0:
            print("Game Over")

    def move(self):
        pass

    def attack(self, monster):
        monster.hp -= self.dmg

    def check_room(self, room):
        pass

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description