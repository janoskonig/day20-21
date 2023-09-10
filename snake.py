from turtle import Turtle
MOVE_DISTANCE = 20
class Snake:
    """Models the snake's movements, lengthens the snake, and much more"""
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(x=0 - (_ * 20), y=0)
            self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)