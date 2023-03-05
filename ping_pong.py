import turtle

# Set up the game window
window = turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=600, height=400)

# Create the paddles
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-250, 0)

right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("pink")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Set up the score display
score_left = 0
score_right = 0
score = turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 170)
score.write("player1: {}  player 2: {}".format(score_left, score_right), align="center", font=("Courier", 16, "normal"))

# Define the paddle movement functions
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Bind the paddle movement functions to keys
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with the walls
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Check for collisions with the paddles
    if (ball.xcor() < -240 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50) or (ball.xcor() > 240 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.dx *= -1

    # Check for scoring
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        score.clear()
        score.write("player 1: {}  player 2: {}".format(score_left, score_right), align="center", font=("Courier", 16, "normal"))

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
