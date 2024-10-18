from time import sleep
from threading import Thread
from random import randint, choice

class Warrior:
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100

    def attack(self, other) -> None:
        other.health -= 20
        print(f'{self.name} атакует {other.name}. У {other.name} осталось {other.health} очков здоровья.')
        random_time_attack = randint(1, 3)
        sleep(random_time_attack)

def fight(warrior1: Warrior, warrior2: Warrior) -> None:
    while warrior1.health > 0 and warrior2.health > 0:
        attacker = choice([warrior1, warrior2])
        defender = warrior2 if attacker == warrior1 else warrior1
        attacker.attack(defender)

        if defender.health <= 0:
                print(f'{attacker.name} побеждает!')
                break


warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

thread = Thread(target=fight(warrior1, warrior2))

thread.start()

thread.join()
