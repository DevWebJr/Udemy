import turtle

#marches à escalader
def climb(value, repeat):
    target = turtle.Turtle()
    step = 0
    while step < repeat:
        target.forward(value)
        target.left(90)
        target.forward(value)
        target.right(90)
        step += 1
    
    target.forward(value)


def draw_a_square(value):
    target = turtle.Turtle()
    for i in range(0, 4):
        target.forward(value)
        target.left(90)
    return value
        

def draw_many_squares(initial_size):
    number = ""
    while number == "":
        try:
            number = int(input("How many square ? "))
            for i in range(0, number):
                new_size = (i+1)*initial_size
                draw_a_square(new_size)
        except ValueError:
            number = int(input("You have to enter a number : "))
