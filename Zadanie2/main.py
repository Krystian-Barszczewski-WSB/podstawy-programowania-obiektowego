from Zadanie2.CrawlerGame import Hero, Monster, Goblin, Dungeon

def main():
    dungeon = Dungeon()
    dungeon.generate_map()
    hero = Hero(15, 10, dungeon.rooms[(0,0)])

if __name__ == '__main__':
    main()