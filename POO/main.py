# import Person
from Person import *

if __name__ == '__main__':
    family_member_01 = Person("Giannotta","Tito", 38,True)
    family_member_02 = Person("Giannotta", "Lio", 32, False)
    family_member_03 = Person("Giannotta", "Shemsedine", 10, True)
    family_member_04 = Person("Giannotta", "Souleyman", 9, True)
    family_member_05 = Person("Giannotta", "Bilel", 7, True)
    family_member_06 = Person("Giannotta", "Hafsa", 5, False)
    family_member_07 = Person("Giannotta", "OubaydoulLah", 3, True)
    
    family = (family_member_01, family_member_02,
              family_member_03, family_member_04, family_member_05, family_member_06, family_member_07)
    for each_one in family:
        each_one.To_Present()
