from Snake_ import Snake
import food
import ScoreBoard
import time
from turtle import Turtle,Screen
tim=Turtle()
sn=Snake()
fd=food.Food()
sb=ScoreBoard.ScoreBoard()
scr=Screen()


scr.setup(height=600,width=600)
scr.bgcolor('black')
scr.title("My snake game")
scr.tracer(0)
scr.listen()

scr.onkey(fun=sn.up,key="Up")
scr.onkey(fun=sn.down,key="Down")
scr.onkey(fun=sn.left,key="Left")
scr.onkey(fun=sn.right,key="Right")

tim.color("red")
tim.penup()
tim.goto(-280,270)
tim.pendown()
tim.fd(560)
tim.rt(90)
tim.fd(560)
tim.rt(90)
tim.fd(560)
tim.rt(90)
tim.fd(560)
tim.rt(90)
tim.hideturtle()

game_is_on=True

while game_is_on:
    scr.update()
    if sb.score>5:
        time.sleep(0.1)
    elif sb.score>10:
        time.sleep(0.3)
    elif sb.score>15:
        time.sleep(0.05)
    else :
        time.sleep(0.6)

    sn.MOVING_S()

    if sn.head.distance(fd) < 15:
        print('nom nom nom')
        sb.Score_in()
        sb.updateScore()
        sn.Extends()
        fd.refresh()

    elif  sn.head.xcor()>=285 or sn.head.xcor()<=-285 or sn.head.ycor()>=270 or sn.head.ycor()<=-285 :
        print("end")
        # sb.gameover()
        sb.reset()        # game_is_on=False
        sn.reset()
    for degment in sn.segments:
        if  degment==sn.head:
            pass
        elif sn.head.distance(degment)<10:
            sb.reset()
            sn.reset()
            # sb.gameover()
            # game_is_on = False








scr.exitonclick()