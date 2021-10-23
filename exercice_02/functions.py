import CONST


def ask_number():
    number = 0
    while True:
        try:
            number = int(input("Quel est le nombre magique ? "))
        except:
            number = int(input("Le nombre magique est un nombre, réessayez : "))
        False
        return number
    

def verify_number(user_number):
    number = CONST.MAGICAL_NUMBER

    user_number = 0
    while not user_number == number:
        if user_number == number:
            print("Bien joué!\nVous avez gagné!")
        elif user_number > number:
            print("Le nombre magique est plus petit.")
        else:
            print("Le nombre magique est plus grand.")
            
    return user_number
