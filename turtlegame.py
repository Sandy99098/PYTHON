import turtle

# # Set up the screen
# wn = turtle.Screen()
# wn.title("Turtle Graphics - Rectangle")  # Set the window title

# # Create a turtle named bob
# bob = turtle.Turtle()

# # Function to draw a rectangle
# def draw_rectangle(t, width, height):
#     for i in range(2):
#         t.forward(width)
#         t.right(90)
#         t.forward(height)
#         t.right(90)

# # Draw a rectangle with width 150 and height 100
# draw_rectangle(bob, 150, 100)

# # This will keep the window open until you click on it
# wn.exitonclick()

wn=turtle.Screen()
wn.bgcolor("green")
a=turtle.Turtle()
a.pensize(5)
a.pencolor("black")
a.color("white")



a.forward(150)
a.left(90)
a.forward(50)
a.left(90)
a.forward(150)
a.left(90)
a.forward(50)

#  b movement 
b=turtle.Screen()
b=turtle.Turtle()
b.pensize("9")
b.pencolor("blue")
b.left(180)
b.forward(300)
b.right(45)
b.left(135)
b.forward(300)
b.left(135)
b.forward(425)

#  for circle
b.pencolor("red")
b.penup()
b.forward(200)
b.pendown()
b.circle(60)

# exit on clicking somewehere
wn.exitonclick()

