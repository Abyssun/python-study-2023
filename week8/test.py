
import turtle
# 设置画布和画笔
canvas = turtle.Screen()
pen = turtle.Turtle()
# 设置画笔颜色和宽度
pen.color("green")
pen.width(3)
# 绘制花枝
pen.up()
pen.goto(-200, 0)
pen.down()
for i in range(8):
    pen.forward(50)
    pen.right(45)
    pen.forward(50)
    pen.right(135)
    pen.forward(50)
    pen.right(45)
    pen.forward(50)
    pen.right(135)
    pen.right(45)
# 绘制花瓣
pen.up()
pen.goto(0, 0)
pen.down()
for i in range(10):
    pen.circle(50)
    pen.right(36)
# 绘制太阳
pen.up()
pen.goto(200, 200)
pen.down()
pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()
# 绘制草地
pen.up()
pen.goto(-250, -200)
pen.down()
pen.color("green")
pen.begin_fill()
pen.forward(500)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(500)
pen.right(90)
pen.forward(100)
pen.end_fill()
# 隐藏画笔
pen.hideturtle()
# 关闭画布
canvas.exitonclick()

