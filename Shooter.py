#polymorphism class

class Shooter:
    #Creating a construcor for accept parameters
    def __init__(self, type, name, age, experience):
        self._name = name
        self._age = age
        self._experience = experience
        self._type = type

    def show(self):
        return f"{self._type} Name of shooter {self._name} \nAge {self._age}\nExperience {self._experience}\n"