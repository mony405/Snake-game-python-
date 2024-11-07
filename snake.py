from turtle import Turtle
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.seg = []
        self.creatsnake()
        self.head = self.seg[0]

    def creatsnake(self):
        for POS in POSITIONS:
            self.add_seg(POS)


    def add_seg(self,pos):
        square = Turtle(shape="circle")
        square.color("white")
        square.penup()
        square.goto(pos)
        self.seg.append(square)
    def reset_snake(self):
        for s in self.seg:
            s.goto(1000,1000)
        self.seg.clear()
        self.creatsnake()
        self.head=self.seg[0]

    def extend(self):
        # add new segment to snake
        self.add_seg(self.seg[-1].position())


    # ------------------------------------
    def move(self):
        for sq_num in range(len(self.seg) - 1, 0, -1):
            x = self.seg[sq_num - 1].xcor()
            y = self.seg[sq_num - 1].ycor()
            self.seg[sq_num].goto(x, y)
        self.seg[0].forward(MOVE)


    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading( DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading( LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)