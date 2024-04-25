from turtle import Turtle,Screen

STARTING_CORDINATES=[(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE=20


class Snake():
    def __init__(self):
        self.segments=[]
        self.Create_snake()
        self.head=self.segments[0]
        self.MOVING_S()
        self.up()
        self.down()
        self.left()
        self.right()



    def  Create_snake(self):
        for _ in STARTING_CORDINATES:
            self.add_segment(_)


    def MOVING_S(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self,_):
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(_)
        self.segments.append(new_segment)

    def Extends(self):
        self.add_segment(self.segments[-1].pos())

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # if self.head.heading() != 180:
        self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.Create_snake()
        self.head=self.segments[0]