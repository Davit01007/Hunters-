from Shooter import *
import random

#crathing a class who inherits 'main' other class.
class Beginner(Shooter):

    def __init__(self, name, age, experience):
        super().__init__("Beginner's", name, age, experience)

#__str__ for method for take a coustom adrees in atributes
    def __str__(self):
        return "Beginner"

#Counting a hit probability, then we compare the received answer with a random number.
#Then we would know if the numbers are even return True, else False.
    def shoot(self):
        hit_probability = 0.01 * self._experience
        print(f"Hit probability:\t {hit_probability}")

        random_number = random.uniform(0.01, 1)
        print(f"Random number:\t {random_number}")

        shoot_result = random_number <= hit_probability
        print(f"1. Beginner: Result of shoot {shoot_result}")

        result = True if shoot_result else False
        return result
