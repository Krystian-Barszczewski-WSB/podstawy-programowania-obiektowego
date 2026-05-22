from Zadanie2.CrawlerGame import Hero, Monster


def main():
    hero = Hero(100, 10)
    monster = Monster("Vampire", 20, 5)

    print(hero.hp)
    print(monster.hp)

    hero.attack(monster)

    print(monster.hp)

if __name__ == '__main__':
    main()