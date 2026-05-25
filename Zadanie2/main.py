from unittest import case

from Zadanie2.CrawlerGame import Hero, Monster, Goblin, Dungeon

def main():
    dungeon = Dungeon()
    dungeon.generate_map()
    hero = Hero(100, 10, dungeon)

    while True:
        hero.action_menu()


if __name__ == '__main__':
    main()