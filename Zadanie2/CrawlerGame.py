#Gra Dungeon crawler (podziemia) – klasy Hero, Monster, Room, Item, Dungeon;
# przemieszczanie się między pomieszczeniami, walka, zbieranie skarbów.
import random

class Dungeon:
    def __init__(self, max_rooms = 14):
        self.rooms = {(0, 0): Room(0, 0)}
        self.rooms[(0, 0)].generate_rooms(self.rooms, max_rooms)

        while len(self.rooms) < 6:
            self.rooms.clear()
            self.rooms = {(0, 0): Room(0, 0)}
            self.rooms[(0, 0)].generate_rooms(self.rooms, max_rooms)

        last_room = list(self.rooms.keys())[-1]
        self.rooms[last_room].monster = Dragon()

        xs = [pos[0] for pos in self.rooms]
        ys = [pos[1] for pos in self.rooms]

        self.min_x, self.max_x = min(xs), max(xs)
        self.min_y, self.max_y = min(ys), max(ys)

    def generate_map(self, hero_pos = (0, 0)):
        last_room = list(self.rooms.keys())[-1]

        for y in range(self.max_y, self.min_y - 1, -1):
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) in self.rooms:
                    if (x, y) == hero_pos:
                        print("◯", end=" ")
                    elif (x, y) == last_room:
                        print("▼", end=" ")
                    elif self.rooms[(x, y)].monster:
                        print("⚠", end=" ")
                    else:
                        print("■", end=" ")
                else:
                    print("░", end=" ")
            print()


class Room:
    def __init__(self, x, y):
        self.loot = []
        self.monster = None
        self.x = x
        self.y = y
        #self.neighboring_rooms = neighboring_rooms # 0-north, 1-south, 2-east, 3-west
        #self.generate()

    def generate(self):
        if random.random() < 0.3:
            self.loot = Item("HP Potion", "Heals the users wounds")
        if random.random() < 0.6:
            self.monster = Goblin()

    def generate_rooms(self, rooms, max_rooms):
        if len(rooms) >= max_rooms:
            return

        for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
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

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

        if self._hp <= 0:
            del self

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
        how_much = random.randint(1, 15)
        print(f"Goblin steals {how_much} gold from you!")
        hero.gold -= how_much

class Dragon(Monster):
    def __init__(self):
        super().__init__(
            name="Dragon",
            hp=120,
            dmg=15,
            gold_drop=1000
        )
        self.counter = 0

    def use_skill(self, hero):
        if self.counter <= 0:
            print("The dragon is preparing a powerful attack! Next time it uses a skill it will deal massive damage!")
            self.counter += 1
        elif self.counter > 0:
            self.counter = 0
            print(f"FDragon breaths fire on you dealing 40 damage!")
            hero.hp -= 40


class Hero:
    def __init__(self, hp, dmg, dungeon):
        self._hp = hp
        self.dmg = dmg
        self.inventory = []
        self._gold = 0
        self.dungeon = dungeon
        self.rooms = dungeon.rooms
        self.current_room = dungeon.rooms[(0, 0)]
        self.is_defending = False

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
        if not self.is_defending:
            self._hp = value
        else:
            self._hp = self.hp + (value - self._hp) * 0.5

        if self._hp <= 0:
            print("Game Over")

        self.is_defending = False

    def action_menu(self):
        choice = input("Choose your action (M-ove, C-heck, F-fight, L-oot, S-tatus): ").upper()

        match choice:
            case "M":
                self.move()
                self.dungeon.generate_map((self.current_room.x, self.current_room.y))
            case "C":
                pass
            case "F":
                if self.current_room.monster:
                    self.attack(self.current_room.monster)
                    self.dungeon.generate_map((self.current_room.x, self.current_room.y))
                else: print("There is nothing to fight")
            case "L":
                self.check_room(self.current_room)
            case "S":
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(f"  HP: {self.hp}")
                print(f"  Gold: {self.gold}")
                print(f"  Items: {self.inventory}")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    def move(self):
        if self.current_room.monster:
            print("A monster is blocking your path!")
            return

        print("You can move to room(s):", end=" ")
        self.current_room.generate_rooms(self.rooms, self._gold)
        possible_directions = []

        for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_pos = (self.current_room.x + pos[0], self.current_room.y + pos[1])

            if new_pos in self.rooms:
                match pos:
                    case (0, 1):
                        print("N-orth,", end=" ")
                    case (0, -1):
                        print("S-outh,", end=" ")
                    case (1, 0):
                        print("E-ast,", end=" ")
                    case (-1, 0):
                        print("W-est,", end=" ")
                possible_directions.append(pos)

        print()
        direction = input("Which direction would you like to move to? ").upper()
        match direction:
            case "N":
                if (0, 1) in possible_directions:
                    self.current_room = self.rooms[(self.current_room.x, self.current_room.y + 1)]
                else: print("Can't go there.")
            case "S":
                if (0, -1) in possible_directions:
                    self.current_room = self.rooms[(self.current_room.x, self.current_room.y - 1)]
                else: print("Can't go there.")
            case "E":
                if (1, 0) in possible_directions:
                    self.current_room = self.rooms[(self.current_room.x + 1, self.current_room.y)]
                else: print("Can't go there.")
            case "W":
                if (-1, 0) in possible_directions:
                    self.current_room = self.rooms[(self.current_room.x - 1, self.current_room.y)]
                else: print("Can't go there.")

    def attack(self, monster):
        while monster.hp > 0 and self.hp > 0:
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(f"  {monster.name}: {monster.hp} HP")
            print(f"  You: {self.hp} HP")
            print(f"  A-ttack   C-check")
            print(f"  D-efend   I-tems")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

            choice = input("Choose your action: ").upper()

            match choice:
                case "A":
                    print(f"You attacked the {monster.name} for {self.dmg}!")
                    monster.hp -= self.dmg
                case "C":
                    print(f"A {monster.name}, has {monster.hp} health and deals {monster.dmg} damage each turn.")
                case "D":
                    print(f"You defend yourself making the incoming attack deal {monster.dmg * 0.5} (50%) less damage!")
                    self.is_defending = True
                case "I":
                    print(self.inventory)

            if monster.hp > 0:
                if random.random() < 0.25:
                    print(f"{monster.name} uses a skill!")
                    monster.use_skill(self)
                else:
                    print(f"{monster.name} has attacked you for {monster.dmg}!")
                    monster.attack(self)
            else:
                print(f"{monster.name} has been defeated!")

        if self.hp > 0:
            print("You won!")
            self.current_room.monster = None
        else:
            print("You lost!")

    def check_room(self, room):
        print("You check the room for items and find: ")
        print(room.loot)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description