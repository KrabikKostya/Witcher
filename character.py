from abc import ABC, abstractmethod


class Field:
    melleRow = []
    rangedRow = []


class Character(ABC):
    def __init__(self, name, hp, weapon, attackDMG, spawn):
        self.name = name  #attckDMG_crit,
        self.hp = hp
        self.weapon = weapon
        self.attackDMG = attackDMG
        self.spawn = spawn

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
    def __init__(self, name, hp,  weapon, attackDMG, spawn, maxAge, origin, fertility, xenofobia):
        super().__init__(name, hp, weapon, attackDMG, spawn)
        self.maxAge = maxAge
        self.origin = origin # what do we hae to write in here?
        self.fertility = fertility
        self.xenophobia = xenofobia

    def move():
        pass
    def attack():
        pass
    def desision():
        pass
    def look():
        pass


class Witcher(Human):
    def __init__(self, name, hp, weapon, attackDMG, spawn, maxAge, origin, fertility, xenofobia):
        super().__init__(name, hp, weapon, attackDMG, spawn, maxAge, origin, fertility, xenofobia)
        hp = 20


class Wizard(Human):
    pass

# geralt = Witcher('Geralt', )
geralt = Witcher('Geralt', 200, 'sword', 30, [3, 4], 250, 'mutant', False, True)
print(geralt)


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
