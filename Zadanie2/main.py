from unittest import case

from Zadanie2.CrawlerGame import Hero, Monster, Goblin, Dungeon

def main():
    dungeon = Dungeon()
    dungeon.generate_map()
    hero = Hero(15, 10, dungeon.rooms)

    while True:
        choice = input("Choose your action (M-ove, C-heck, A-ttack, L-oot, S-tatus): ").upper()

        match choice:
            case "M":
                hero.move()
            case "C":
                pass
            case "A":
                hero.attack(hero.current_room.monsters[0])
            case "L":
                pass
            case "S":
                pass
        dungeon.generate_map((hero.current_room.x, hero.current_room.y))


if __name__ == '__main__':
    main()