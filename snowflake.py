import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main(size, order):

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake Fractal")
    
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(0)  # Set the drawing speed to the fastest
    
    # Position the turtle
    fractal_turtle.penup()
    fractal_turtle.goto(-150, 90)
    fractal_turtle.pendown()
    
    # Draw the Koch snowflake
    for _ in range(3):
        koch_snowflake(fractal_turtle, order, size)
        fractal_turtle.right(120)
    
    window.mainloop()

if __name__ == "__main__":
    print ('welcome to snowflake fractal generator')
    # 1: Spørg brugeren om Size
    # 2: Hvis den ikke er indenfor 100-300, så gå ned i while loop
    # 3: Forbliv i while loop, indtil bruger har givet en rigtig værdi for size
    size = int(input('hvad skal størelsen være på din snefnuk vælg et tal mellem 100 og 300: '))
    while (size < 100 or size > 300):
        print('whoops wrong input')
        size = int(input('hvad skal størelsen være på din snefnuk vælg et tal mellem 100 og 300: '))

    order = int(input('hvad for en order vil du have 1, 2, 3 eller 4: '))
    while (order < 1 or order > 4):
        print('whoops wrong input')
        order = int(input('hvad for en order vil du have 1, 2, 3 eller 4: '))

       
    main(size, order)

    print ('thank you for using snowflake fractal generator')