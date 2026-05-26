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
        self.loot = None
        self.monster = None
        self.x = x
        self.y = y
        #self.neighboring_rooms = neighboring_rooms # 0-north, 1-south, 2-east, 3-west
        #self.generate()

    def generate(self):
        if random.random() < 0.4:
            self.loot = HPPotion()
        elif random.random() < 0.6:
            self.loot = Bomb()

        if random.random() < 0.6:
            if random.random() < 0.5:
                self.monster = Goblin()
            else:
                self.monster = Wolf()

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
            print(f"Dragon breathes fire on you dealing 40 damage!")
            hero.hp -= 40

class Wolf(Monster):
    def __init__(self):
        super().__init__(
            name="Wolf",
            hp=25,
            dmg=10,
            gold_drop=100
        )

    def use_skill(self, hero):
        how_much = random.randint(5, 15)
        print(f"Wolf howls making it's HP grow by {how_much}!")
        self.hp += how_much

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
        self.kills = 0
        self.has_won = False

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
        choice = input("Choose your action (M-ove, F-fight, L-oot, S-tatus): ").upper()

        match choice:
            case "M":
                self.move()
                self.dungeon.generate_map((self.current_room.x, self.current_room.y))
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
                print(f"  Items: {[item.name for item in self.inventory]}")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    def move(self):
        if self.current_room.monster:
            print("A monster is blocking your path!")
            return

        print("You can move to room(s):", end=" ")
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
        self.dungeon.generate_map((self.current_room.x, self.current_room.y))
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
            print(f"   {monster.name}: {monster.hp} HP")
            print(f"   You: {self.hp} HP")
            print(f"   A-ttack   C-check")
            print(f"   D-efend   I-tems")
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
                    if not self.inventory:
                        print("Inventory is empty")
                        continue

                    for i, item in enumerate(self.inventory, 1):
                        print(f"{i}. {item.name}")

                    print(f"{len(self.inventory) + 1}. Exit Inventory")

                    choice = int(input("What do you want to do? "))

                    if choice == len(self.inventory) + 1:
                        continue

                    item = self.inventory[choice - 1]
                    item.use(self)

                    self.inventory.remove(item)

            if monster.hp > 0:
                if random.random() < 0.25:
                    print(f"{monster.name} uses a skill!")
                    monster.use_skill(self)
                else:
                    print(f"{monster.name} has attacked you for {monster.dmg}!")
                    monster.attack(self)
            else:
                print(f"{monster.name} has been defeated!")
                print(f"Obtained {monster.gold_drop} gold!")
                self.gold += monster.gold_drop
                self.kills += 1

        if self.hp > 0:
            if isinstance(monster, Dragon):
                print("You Have slain the boss!")
                self.has_won = True
                self.current_room.monster = None
                return
            print("You won the battle!")
            self.current_room.monster = None
        else:
            print("You lost!")

    def check_room(self, room):
        if not room.loot:
            print("You check the room... but find nothing")
            return

        print("You check the room for items and find: ")
        print(room.loot.name + " - " + room.loot.description)
        choice = input("Do you want to pick it up? (Y/N) ").upper()
        if choice == "Y":
            self.inventory.append(room.loot)
            room.loot = None
        else:
            print("You left it.")

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, hero):
        pass

class HPPotion(Item):
    def __init__(self):
        super().__init__(
            "HP Potion",
            "Heals the users wounds"
        )

    def use(self, hero):
        hero.hp += 35
        print(f"You healed 35 HP!")

class Bomb(Item):
    def __init__(self):
        super().__init__(
            "Bomb",
            "Deals big damage to enemies"
        )

    def use(self, hero):
        hero.current_room.monster.hp -= 40
        print(f"You dealt 40 damage to the monster!")