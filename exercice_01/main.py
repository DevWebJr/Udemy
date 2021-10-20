import turtle
import functions



if __name__ == '__main__':
    # functions.climb(30, 5)
    value = ""
    while value == "":
        try:
            value = int(input("Enter value : "))
        except ValueError:
            value = int(input("You have to enter a number : "))
            
    size = functions.draw_a_square(value)
    
    
                
    functions.draw_many_squares(size)
    
    turtle.done()
    
