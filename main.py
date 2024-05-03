import turtle
import winsound

# window 
wn = turtle.Screen() # creating new screen object/window from turtle module - represents where elements will be drawn - assigned to variable wn
wn.title("Pong") # sets title of the window
wn.bgcolor("black") # sets background colour of window
wn.setup(width=800, height=600) # sets dimensions of the window
wn.tracer(0) # tracer called with argument of 0 allows drawing operations to be more efficient

# score variables both set to 0
score_a = 0
score_b = 0

# variable paddle_a and attributes for it
paddle_a = turtle.Turtle() # creates new turtle object called paddle_a allowing for graphics
paddle_a.speed(0) # sets speed of turtle to the fastest (0)
paddle_a.shape("square") # shape of turtle is set to square
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # changes size of the turtle shape
paddle_a.color("white") # sets colour of the turtle
paddle_a.penup() # turtle will not draw anything when it moves
paddle_a.goto(-350, 0) # moves turtle to these specific coordinates (to the left hand side of the window)

# variable paddle_b and attributes for it
paddle_b = turtle.Turtle() # creates new turtle object called paddle_b allowing for graphics
paddle_b.speed(0) # sets speed of turtle to the fastest (0)
paddle_b.shape("square") # shape of turtle is set to square
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # changes size of the turtle shape
paddle_b.color("white") # sets colour of the turtle
paddle_b.penup() # turtle will not draw anything when it moves
paddle_b.goto(350, 0) # moves turtle to these coordinates (to the right hand side of the window)

# variable ball and attributes for it
ball = turtle.Turtle() # creates new turtle object ball allowing for graphics
ball.speed(0) # sets speed of turtle to the fastest (0)
ball.shape("square") # shape of turtle is set to square
ball.color("white") # sets colour of the turtle
ball.penup() # turtle will not draw anything when it moves
ball.goto(0, 0) # moves turtle to these coordinates (to the centre of the window)
ball.dx = 0.15  # speed of the balls x coordinate
ball.dy = 0.15  # speed of the balls y coordinate

# variable pen and attributes for it
pen = turtle.Turtle() # creates new turtle object pen allowing for graphics
pen.speed(0) # sets speed of turtle to the fastest (0)
pen.color("white") # sets colour of the turtle
pen.penup() # turtle will not draw anything when it moves
pen.hideturtle() # hides the trail that the turtle cursor leaves behind
pen.goto(0, 260) # moves turtle to these coordinates (top of the window)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) # prints this text at location of turtle cursor

line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.shapesize(stretch_wid=32, stretch_len=0.1)
line.color("white")
line.penup()
line.goto(0,0)

# finds the x/y coordinate and assigns them to x/y - consequently, pixels are added or removed based on function name then those values are set as new turtle coordinates
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20 
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 20
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20 
    paddle_b.sety(y)

wn.listen() # tells screen to listen for keyboard input - calls said function when "x" is pressed - allows for paddle movement
wn.onkeypress(paddle_a_up, "w") 
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop (main code) and everytime this loop runs, it updates the screen
while True:
    wn.update()

    # takes current x/y coordinate of ball and adds some ball.dx or ball.dy value, updating balls current position
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # if the ball touches top of the window, reset the ball's y coordinate to 290 and flip its coordinates so that it appears the ball has bounced
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 
        winsound.PlaySound("pingpong1.wav", winsound.SND_ASYNC) # sound is played each "bounce"

    # if the ball touches bottom of the window, reset the ball's y coordinate to -280 and flip its coordinates so that it appears the ball has bounced
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1  
        winsound.PlaySound("pingpong1.wav", winsound.SND_ASYNC) # sound is played each "bounce"

    # resetting balls position to the middle paddle_a receives point
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1 # after a point, the ball will travel in the opposite direction in which it travelled before
        # score keeping
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # resetting balls position after each point
    if ball.xcor() < -405:
        ball.goto(0, 0)
        ball.dx *= -1
        # score keeping
        score_b += 1
        pen.clear() # clear previous score to write the new score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if ball.xcor() > 330 and (ball.xcor() < 350 and paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40): # checks if the ball's x-coordinate is within a certain range and if the ball's y-coordinate is within a certain range relative to paddle_b's y-coordinate
        ball.setx(330) # sets the ball to a position just in front of the paddle
        ball.dx *= -1 # flips the balls flow of direction
        winsound.PlaySound("pingpong2.wav", winsound.SND_ASYNC) # sound of bouncing off paddle

    if ball.xcor() < -330 and (ball.xcor() > -350 and paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40): # checks if the ball's x-coordinate is within a certain range and if the ball's y-coordinate is within a certain range relative to paddle_a's y-coordinate
        ball.setx(-330) # sets the ball to a position just in front of the paddle
        ball.dx *= -1 # flips the balls flow of direction
        winsound.PlaySound("pingpong2.wav", winsound.SND_ASYNC) # sound of bouncing off paddle

    # restricting paddles from going off-screen
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)
