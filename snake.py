from turtle import Turtle

TURTLE_SIDE_SIZE = 20
SNAKE_STARTING_LEN = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, SNAKE_STARTING_LEN):
            position = (i*-TURTLE_SIDE_SIZE, 0)
            self.add_segment(position)

    def move(self):
        """ move the snake in it's current direction """
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
        self.head.forward(TURTLE_SIDE_SIZE)

    def up(self):
        """ turn snake to face up if not currently facing down """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ turn snake to face down if not currently facing up """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ turn snake to face left if not currently facing right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ turn snake to face right if not currently facing left """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.segments.append(t)