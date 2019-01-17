# snake game
# https://www.youtube.com/watch?v=BP7KMlbvtOo

import turtle
import time
import random

# constants
delay = 0.1

# variables
segments = []
score = 0
high_score = 0

# init screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# init head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# init food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
x = round(random.randint(-280,280) / 20) * 20
y = round(random.randint(-280,280) / 20) * 20
food.goto(x,y)

# init score
text = turtle.Turtle()
text.speed(0)
text.shape("square")
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write(
  "Score: 0 High Score: 0",
  align="center",
  font=("Courier", 24, "normal")
)

# functions
def reset():
  time.sleep(1)
  head.goto(0,0)
  head.direction = "stop"
  reset_segments()
  reset_score()

def move_head():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y+20)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y-20)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x+20)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x-20)

def go_up():
  if not head.direction == "down":
    head.direction = "up"

def go_left():
  if not head.direction == "right":
    head.direction = "left"

def go_down():
  if not head.direction == "up":
    head.direction = "down"

def go_right():
  if not head.direction == "left":
    head.direction = "right"

def grow():
  new_segment = turtle.Turtle()
  new_segment.speed(0)
  new_segment.shape("square")
  new_segment.color("grey")
  new_segment.penup()
  segments.append(new_segment)

def move_food():
  x = round(random.randint(-280,280) / 20) * 20
  y = round(random.randint(-280,280) / 20) * 20
  food.goto(x,y)

def move_segments():
  # other segments
  for index in range(len(segments)-1,0,-1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)
  # first segment
  x = head.xcor()
  y = head.ycor()
  segments[0].goto(x,y)

def check_border_collision():
  if head.ycor()>= 300 or head.ycor()<=-300 or head.xcor()>= 300 or head.xcor()<=-300:
    reset()

def check_segment_collision():
  for segment in segments:
    if segment.distance(head) < 20:
      reset()

def increase_score():
  global score
  global high_score
  score += 10
  if score > high_score:
    high_score = score
  text.clear()
  text.write(
    "Score: {} High Score: {}".format(score,high_score),
    align="center",
    font=("Courier", 24, "normal")
  )

def reset_score():
  global score
  score = 0
  text.clear()
  text.write(
    "Score: 0 High Score: {}".format(high_score),
    align="center",
    font=("Courier", 24, "normal")
  )

def reset_segments():
  global segments
  for segment in segments:
    segment.hideturtle()
  segments.clear()

def increase_speed():
  global delay
  delay -= 0.002

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(wn.bye, "q")

# main gameloop
while True:
  wn.update()
  if head.distance(food) < 20:
    increase_score()
    move_food()
    increase_speed()
    grow()
  if len(segments) > 0:
    move_segments()
  move_head()
  check_border_collision()
  check_segment_collision()
  time.sleep(delay)

wn.mainloop()
