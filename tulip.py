import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create a turtle named "tulip"
tulip = turtle.Turtle()
tulip.speed(10)

# Function to draw a petal
def draw_petal():
    tulip.begin_fill()
    tulip.circle(20, 60)
    tulip.left(120)
    tulip.circle(20, 60)
    tulip.left(120)
    tulip.circle(20, 60)
    tulip.end_fill()

# Function to draw the stem
def draw_stem(length):
    tulip.color("green")
    tulip.pensize(3)
    tulip.penup()
    tulip.right(90)
    tulip.forward(10)
    tulip.right(90)
    tulip.pendown()
    tulip.forward(length)
    tulip.penup()
    tulip.right(90)
    tulip.forward(10)
    tulip.right(90)
    tulip.pendown()
    tulip.forward(length)
    tulip.right(90)

# Function to draw a leaf
def draw_leaf():
    tulip.color("green")
    tulip.begin_fill()
    tulip.circle(50, 60)
    tulip.left(120)
    tulip.circle(50, 60)
    tulip.end_fill()

# Function to draw a single tulip flower
def draw_tulip(x, y, stem_length):
    tulip.penup()
    tulip.goto(x, y)
    tulip.pendown()

    # Draw the stem
    draw_stem(stem_length)

    # Draw the petals
    tulip.penup()
    tulip.goto(x, y + stem_length)
    tulip.pendown()
    tulip.color("red")
    tulip.setheading(60)
    for _ in range(3):
        draw_petal()
        tulip.right(120)

    # Draw the leaves
    tulip.penup()
    tulip.goto(x, y + stem_length / 2)
    tulip.setheading(150)
    tulip.pendown()
    draw_leaf()
    tulip.penup()
    tulip.goto(x, y + stem_length / 2)
    tulip.setheading(30)
    tulip.pendown()
    draw_leaf()

# Draw a bouquet of tulips
draw_tulip(-50, -200, 150)
draw_tulip(0, -200, 180)
draw_tulip(50, -200, 150)
draw_tulip(-100, -220, 140)
draw_tulip(100, -220, 140)


# Hide the tulip turtle
tulip.hideturtle()

# Create a new turtle for the text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.speed(1)
text_turtle.penup()
text_turtle.goto(-150, 50)
text_turtle.pendown()

# Function to write the text with animation
def write_text(message):
    for char in message:
        text_turtle.write(char, font=("Arial", 24, "normal"))
        turtle.delay(100)  # Use turtle.delay to slow down the animation
        text_turtle.penup()
        text_turtle.forward(20)
        text_turtle.pendown()

# Write the message "For you, Razzo"
write_text("Don't be angry , Razzo flower liu")

# Keep the window open until it is closed by the user
screen.mainloop()
