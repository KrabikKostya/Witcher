from abc import abstractmethod, ABC


class Fild:
    melleRow = []
    rangedRow = []
    


class Character(ABC):
    inventory = []
    hp = 0
    attackDNG = 0
    spavn = ""

    def move():
        pass

    def attack():
        pass

    def desision():
        pass

    def look():
        pass


class People(Character):

    maxAge = 80
    skills = []
    name = ""
    origin = "Human"
    fertility = True
    xenophobia = True

    def walk():

        return "walk"


# smth new

