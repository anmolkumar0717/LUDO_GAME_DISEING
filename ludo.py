import turtle
turtle.title("LUDO-GAME")
t=turtle.Turtle()
t.penup()
t.speed(0)
t.goto(-300,300)
t.pendown()
t.pensize(3)
for i in range(4):
    t.fd(600)
    t.right(90)
t.begin_fill()
for j in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("yellow")
t.end_fill()
t.fd(380)
t.begin_fill()
for k in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("red")
t.end_fill()
t.fd(220)
t.right(90)
t.fd(600)
t.right(90)
t.begin_fill()
for i in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("green")
t.end_fill()

t.fd(380)
t.begin_fill()
for k in range(4):
    t.fd(220)
    t.right(90)
t.fillcolor("blue")
t.end_fill()
t.begin_fill()
t.right(90)
t.fd(220)
t.fillcolor("blue")
t.goto(0,0)
t.goto(80,-80)
t.goto(-80,-80)
t.end_fill()
t.begin_fill()
t.fillcolor("yellow")
t.fd(160)
t.goto(0,0)
t.end_fill()
t.begin_fill()
t.fillcolor("red")
t.goto(80,80)
t.goto(-80,80)
t.end_fill()
t.goto(80,80)
t.begin_fill()
t.fillcolor("green")
t.goto(80,-80)
t.goto(0,0)
t.end_fill()
t.penup()
t.goto(300,26)
t.pendown()
t.goto(80,26)
t.penup()
t.goto(80,-26)
t.pendown()
t.goto(300,-26)
t.left(90)
i=44
k=51
t.begin_fill()
t.fillcolor("green")
for j in range(9):
    t.fd(i)
    t.right(90)
    t.fd(k)
    t.right(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.fd(220)
t.end_fill()
t.begin_fill()
t.fillcolor("white")
t.bk(44)
t.left(90)
t.bk(51)
t.left(90)
t.bk(44)
t.end_fill()
for j in range(9):
    t.fd(i)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.fd(220)
t.begin_fill()
t.fillcolor("green")
t.bk(88)
t.left(90)
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.end_fill()
t.bk(105)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
for j in range(8):
    t.fd(i)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.fd(160)
for j in range(10):
    t.fd(i)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        i=44
    else:
        i+=44
t.begin_fill()
t.fillcolor("yellow")
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.end_fill()
t.left(90)
t.bk(132)
t.left(90)
t.fd(53)
t.right(90)
a=44
t.begin_fill()
t.fillcolor("yellow")
for j in range(9):
    t.fd(a)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        a=44
    else:
        a+=44
t.fd(220)
t.end_fill()
t.left(180)
b=44
for j in range(9):
    t.fd(b)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        b=44
    else:
        b+=44
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.begin_fill()
t.fillcolor("white")
t.fd(44)
t.right(90)
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.end_fill()
t.penup()
t.goto(80,80)
t.right(180)
t.pendown()
s=44
for j in range(10):
    t.fd(s)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        s=44
    else:
        s+=44
t.bk(176)
t.left(90)
t.fd(106)
t.right(90)
m=44
for j in range(10):
    t.fd(m)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        m=44
    else:
        m+=44
t.bk(176)
t.right(90)
t.fd(53)
t.left(90)
l=44
t.begin_fill()
t.fillcolor("red")
for j in range(10):
    t.fd(l)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        l=44
    else:
        l+=44
t.end_fill()
t.begin_fill()
t.fillcolor("white")
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.end_fill()
t.begin_fill()
t.fillcolor("red")
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.right(90)
t.fd(44)
t.end_fill()
t.penup()
t.goto(80,-300)
t.pendown()
a=44
for j in range(10):
    t.fd(a)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        a=44
    else:
        a+=44

t.bk(176)
t.left(90)
t.fd(53)
t.right(90)
v=44
t.begin_fill()
t.fillcolor("blue")
for j in range(10):
    t.fd(v)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        v=44
    else:
        v+=44
t.end_fill()
t.bk(176)
t.left(90)
t.fd(53)
t.right(90)
x=44
for j in range(10):
    t.fd(x)
    t.left(90)
    t.fd(53)
    t.left(90)
    if j%2==0:
        x=44
    else:
        x+=44
t.bk(176)
t.begin_fill()
t.fillcolor("white")
t.fd(44)
t.right(90)
t.fd(53)
t.right(90)
t.fd(44)
t.right(90)
t.fd(53)
t.end_fill()
t.begin_fill()
t.fillcolor("blue")
t.right(90)
t.fd(88)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.left(90)
t.fd(53)
t.left(90)
t.fd(44)
t.end_fill()
t.left(90)
t.penup()
t.goto(260,260)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.left(90)
t.end_fill()
t.penup()
t.goto(260,-260)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-260,-260)
t.right(180)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-260,260)
t.pendown()
t.begin_fill()
t.fillcolor("white")
for i in range(4):
    t.fd(140)
    t.right(90)
t.end_fill()
t.penup()
t.goto(240,240)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t1=turtle.Turtle()
t1.shape("circle")
t1.penup()
t1.goto(220,220)
t1.color("pink")
#######
t.penup()
t.goto(-240,240)
t.right(90)
t.pendown()
t.begin_fill()
t.left(90)
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t2=turtle.Turtle()
t2.shape("circle")
t2.penup()
t2.goto(-220,220)
t2.color("orange")
####1
t.penup()
t.goto(-240,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t3=turtle.Turtle()
t3.shape("circle")
t3.penup()
t3.goto(-220,-220)
t3.color("sky blue")
######2
t.penup()
t.goto(240,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t4=turtle.Turtle()
t4.shape("circle")
t4.penup()
t4.goto(220,-220)
t4.color("lime")
####3
t.penup()
t.goto(180,240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t5=turtle.Turtle()
t5.shape("circle")
t5.penup()
t5.goto(160,220)
t5.color("pink")
t5.penup()
######4
t.penup()
t.goto(-180,240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t6=turtle.Turtle()
t6.shape("circle")
t6.penup()
t6.goto(-160,220)
t6.color("orange")
t6.penup()
####5
t.penup()
t.goto(-180,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t7=turtle.Turtle()
t7.shape("circle")
t7.penup()
t7.goto(-160,-220)
t7.color("sky blue")
t7.penup()
####6
t.penup()
t.goto(180,-240)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t8=turtle.Turtle()
t8.shape("circle")
t8.penup()
t8.goto(160,-220)
t8.color("lime")
t8.penup()
#####7
t.penup()
t.goto(240,180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t9=turtle.Turtle()
t9.shape("circle")
t9.penup()
t9.goto(220,160)
t9.color("pink")
t9.penup()
######8
t.penup()
t.goto(-240,180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t10=turtle.Turtle()
t10.shape("circle")
t10.penup()
t10.goto(-220,160)
t10.color("orange")
####9
t.penup()
t.goto(-240,-180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t11=turtle.Turtle()
t11.shape("circle")
t11.penup()
t11.goto(-220,-160)
t11.color("sky blue")
######10
t.penup()
t.goto(240,-180)
t.pendown()
t.left(90)
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.left(90)
t.end_fill()
t12=turtle.Turtle()
t12.shape("circle")
t12.penup()
t12.goto(220,-160)
t12.color("lime")
######11
t.penup()
t.goto(140,180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t13=turtle.Turtle()
t13.shape("circle")
t13.penup()
t13.goto(160,160)
t13.color("pink")
####
t.penup()
t.goto(-140,180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t14=turtle.Turtle()
t14.shape("circle")
t14.penup()
t14.goto(-160,160)
t14.color("orange")
######
t.penup()
t.goto(-140,-180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("blue")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t15=turtle.Turtle()
t15.shape("circle")
t15.penup()
t15.goto(-160,-160)
t15.color("sky blue")
######
t.penup()
t.goto(140,-180)
t.right(90)
t.pendown()
t.begin_fill()
t.fillcolor("green")
for i in range(4):
    t.fd(40)
    t.right(90)
t.end_fill()
t16=turtle.Turtle()
t16.shape("circle")
t16.penup()
t16.goto(160,-160)
t16.color("lime")
t.penup()
t.goto(-30,0)
t.pendown()
t.write("HOME" ,move='true',font=("arial",16,'normal'))
t.hideturtle()



    























   










