import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Graphics - Rectangle")  # Set the window title

# Create a turtle named bob
bob = turtle.Turtle()

# Function to draw a rectangle
def draw_rectangle(t, width, height):
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

# Draw a rectangle with width 150 and height 100
draw_rectangle(bob, 150, 100)

# This will keep the window open until you click on it
wn.exitonclick()
