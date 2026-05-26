from Zadanie2.CrawlerGame import Hero, Dungeon

def main():
    dungeon = Dungeon()
    dungeon.generate_map()
    hero = Hero(100, 10, dungeon)

    while not hero.has_won:
        if hero.hp > 0:
            hero.action_menu()
        else:
            print(f"Game Over, your looted {hero.gold} gold! And defeated {hero.kills} enemies!")
            return

    print(f"YOU WON! Congratulations, you leave the dungeon with {hero.gold} gold! Having slain {hero.kills} enemies!")
    return

if __name__ == '__main__':
    main()