class Character:
    def __init__(self, race, health, power):
        self.race=race
        self.health=health
        self.power=power

    def attack(self, monster):
        monster.health -=self.power
        if monster == zombie:
            monster.health +=self.power
        print("The {} bashed the {} for {} damage".format(self.race, monster.race, self.power))

    def __str__(self):
        return 'Character: {}, health: {}, power: {}'.format(self.race, self.health, self.power)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def status(self):
        print("{}'s health is at {}".format(self.race, self.health))

hero=Character('Hero', 10, 5)
goblin=Character('Goblin', 6, 2)
wizzard=Character('wizzard',20,1)
zombie=Character("Zombie",20,1)
# print(hero)
# print(goblin)
#
# hero.attack(goblin)
# goblin.attack(hero)
#




# if __name__=="__main__":
while goblin.alive() and hero.alive():
    print("You have {} health and {} power.".format(hero.health, hero.power))
    print("The goblin has {} health and {} power.\n".format(goblin.health, goblin.power))
    print("""What do you want to do:
        1. Fight goblin
        2. Do nothing
        3. Flee!""")
    print(">", end=' ')
    raw_input =input()
    if raw_input == "1":
        hero.attack(goblin)
        if not goblin.alive:
            print("The goblin died!")
    elif raw_input =="2":
        pass
    elif raw_input =='3':
        print("Goodbye!!")
        break
    else:
        print("invalid input {}".format(raw_input))
