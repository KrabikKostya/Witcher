from abc import abstractmethod, ABC


class Field:
    melleRow = []
    rangedRow = []


class Character():
    def __init__(self, skills, name, inventory, hp, attackDMG, spawn):
        self.skills = []
        self.name = ""
        self.inventory = []
        self.hp = 0
        self.attackDMG = 0
        self.spawn = ""

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def attack():
        pass

    @abstractmethod
    def desision():
        pass

    @abstractmethod
    def look():
        pass


class Aen_elle(Character):
    pass


class Dworf(Character):
    pass


class Human(Character):
    def __init__(self, skills, name, inventory, hp, attackDMG, spawn, maxAge, origin, fertility, xenofobia):
        super().__init__(skills, name, inventory, hp, attackDMG, spawn)
        self.maxAge = 80
        self.origin = "Human"
        self.fertility = True
        self.xenophobia = True

    def walk():
        return "walk"


class Witcher(Human):
    def __init__(self, skills, name, inventory, hp, attackDMG, spawn, maxAge, origin, fertility, xenofobia):
        super().__init__(skills, name, inventory, hp, attackDMG, spawn, maxAge, origin, fertility, xenofobia)
        self.hp = 200


class Wizard(Human):
    pass


geralt = Witcher()
print(geralt.hp)

# Gervant geralt
# Excel eskel
# harmful dick A.K.A. lambert lam
# Vasiamyr ves
# Letov-from-kotletov let
# Siri ciri
# Yep yen
# Triss tris
# Keira Merz keira
# Mousevour mysh
# Roshen roshe
# Hlamar hlam
#
#
# Eredine ere
# Imleryh iml
# Karantir car
# Avallak'h ava
#
#
# goldy zol
