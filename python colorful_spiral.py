import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest drawing speed
spiral.width(2)  # Set the pen width

# Number of colors and loops
num_colors = 36
num_loops = 360

for i in range(num_loops):
    # Compute the color for the current loop
    color = colorsys.hsv_to_rgb(i / num_loops, 1.0, 1.0)
    spiral.pencolor(color)
    
    # Move the turtle
    spiral.forward(i * 3 / num_loops + i)
    spiral.left(59)  # Angle to create the spiral effect

# Hide the turtle and finish
spiral.hideturtle()

# Keep the window open until clicked
turtle.done()
