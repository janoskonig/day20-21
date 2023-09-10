from turtle import Screen
from snake import Snake
import time

# Step 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Janos Konig")
screen.tracer(0)

# Step 1: Creating a snake body of 3 little boxes
# segments = []
#
# for _ in range(3):
#     snake = Turtle("square")
#     snake.shapesize(outline=0)
#     snake.penup()
#     snake.color("white")
#     snake.goto(x=0-(_*20),y=0)
#     segments.append(snake)

# Step 2.1: Moving our snake
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg in segments:
#         seg.forward(20)

# Step 2.2: linking the bodies
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)

# Step 2.3: Transitioning to OOP
snake = Snake()
# Step 3: Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


# Step 4:


# Step 5:


# Step 6:
screen.exitonclick()