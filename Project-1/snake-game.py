import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('blue')
wn.setup(width=600, height=600)
wn.tracer(0)

# Head of the snake
head = turtle.Turtle()
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'Stop'

# Food in the game
food = turtle.Turtle()
food.shape(random.choice(['square', 'triangle', 'circle']))
food.color(random.choice(['red', 'green', 'black']))
food.speed(0)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align='center', font=('candara', 24, 'bold'))

# Define movement functions
def group():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goright():
    if head.direction != "left":
        head.direction = "right"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(group, 'w')
wn.onkeypress(godown, 's')
wn.onkeypress(goleft, 'a')
wn.onkeypress(goright, 'd')

segments = []

while True:
    wn.update()

    # Check for collision with border
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, 'bold'))

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add new segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('orange')
        new_segment.penup()
        segments.append(new_segment)

        delay = max(0.05, delay - 0.001)
        score += 10
        high_score = max(high_score, score)

        pen.clear()
        pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, 'bold'))

    # Move the end segments in reverse order
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

    # Move segment 0 to where the head is
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with itself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'Stop'
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

wn.mainloop()
