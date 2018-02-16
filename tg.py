from turtle import *
from random import randint
speed(10)
penup()
goto(-140, 140)

for step in range(16):
	write(step, align='center')
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

ada=Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,120)
ada.pendown()

bob= Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,90)
bob.pendown()

cat= Turtle()
cat.color('yellow')
cat.shape('turtle')

cat.penup()
cat.goto(-160,60)
cat.pendown()

dig= Turtle()
dig.color('black')
dig.shape('turtle')

dig.penup()
dig.goto(-160,30)
dig.pendown()

elf= Turtle()
elf.color('green')
elf.shape('turtle')

elf.penup()
elf.goto(-160,0)
elf.pendown()

for turn in range(100):
	ada.forward(randint(1,5))
	bob.forward(randint(1,5))
	cat.forward(randint(1,5))
	dig.forward(randint(1,5))
	elf.forward(randint(1,5))
