# fun-with-python-for-beginners

# Introduction
Never think that basics of python can ever bore you.There are 2 examples to prove this.
1. A game of Rock Paper Scissors
2. Tortoise race 

# Rock Paper Scissor Game
![alt text](https://github.com/samyuktaprabhu/fun-with-python-for-beginners/blob/master/rps.png)

To begin this game, 
Let us look at the rules first.

![alt text](https://github.com/samyuktaprabhu/fun-with-python-for-beginners/blob/master/rules.jpg)

Rules: 
You and the computer both choose rock, paper or scissors. The winner is decided by these rules:

* Rock blunts scissors

* Paper covers rock

* Scissors cut paper

Cool?

Here goes the code :
```
#!/bin/python3
print("Welcome to the game of rock paper scissor")
print("In this game you will play against the computer.")
print("Rules: You and the computer both choose rock, paper or scissors. The winner is decided by these rules:\nRock blunts scissors\nPaper covers rock\nScissors cut paper")
```
The above code was very simple.
In the next part of the code, We import a library called random which uses randint to generate a random number when ever required.
```
from random import randint
```
In the next part of the code, we implement the main part of the code. THe codes are selfexplanatory as they are associated with comments
```
name=raw_input("Hey there !What's your name?")
comp=0 #Initializing computers score to Zero
player=0 #Initializing players score to zero
while comp<5 and player<5:
  #You is the player/user
	you=raw_input("What do you choose {} ? Rock(r), Paper(p) or scissor(s)?".format(name))
  
	print("Cool!!! You chose {}".format(you))

	print("It is the computers turn now")
	choice=randint(1,3) #chooses random integer for the computer to play.
	
	if choice==1:
		com='r' #rock
	elif choice==2:
		com='p' #paper
	else:
		com='s' #scissors
	print("The computer played {} !".format(com))
 #The codes below are the conditions written to justify the rules of the game. 
	if you==com:
		print("DRAW")
		comp+=1
		player+=1
	elif you=='r' and com=='s':
		print("{} , you win!!!!!!!!!!!!!!!!!!!!!!!!!".format(name))
		player+=1
	elif you=='r' and com=='p':
		print("Oh ! The computer won")
		comp+=1
	elif you=='p' and com=='r':
		print("{} , you win!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(name))
		player+=1
	elif you=='p' and com=='s':
		print("Oh ! The computer won")
		comp+=1
	elif you=='s' and com=='p':
		print("{} , you win!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(name))
		player+=1
	elif you=='s' and com=='r':
		print("Oh ! The computer won")
		comp+=1
	else:
		print("Error occurred,play again")
#This prints the overall result of the game and decides the winner.
if comp==5:
	print("OVERALL CHAMPION : Computer ! :/ ")
else:
	print("OVERALL CHAMPION : {} ! *_* ".format(name))
	
```

The output will be somewhat as follows:

![alt text](https://github.com/samyuktaprabhu/fun-with-python-for-beginners/blob/master/RPSGameOutput.png)

That was quite simple. 

# Tortoise Race

![alt text](https://github.com/samyuktaprabhu/fun-with-python-for-beginners/blob/master/t1.jpg)

In this game, The turtle's are not controlled by the user. Again we use the random randint library to generate the speed of the turtles.

The libraries that we import are turtle and random
Import * means import everything under that library.
```
from turtle import *
from random import randint
```

Next part of the code goes like this

```
speed(10) #speed is 10
penup() #Pull the pen up – no drawing when moving.
goto(-140, 140) #go to this coordinate point (-140,140)
```
Next part fo the code is,
```
for step in range(16):
	write(step, align='center') #Center aligned and needs to move step by step
	right(90) #turn right by 90 degrees
	forward(10) #move forward by 10 units
	pendown() #Pull the pen down – drawing when moving.
	forward(150) #move forward by 150 units
	penup() #Pull the pen up – no drawing when moving.
	backward(160) #move backward by 160 units
	left(90) #turn left by 90 degrees
	forward(20) # move forward by 20 units
```
The next part of the code is where we decide how many turtles will participate in the race and what are their specifications
* You can add any number of turtles as you wish.
```
#Turtle number 1 named Ada
ada=Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,120)
ada.pendown()
```

You can name the turtles accordingly as you wish like I have done here

```
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
```
This part of the code is used to make the turtles run forward where in the randint choses a number on it's own. 
This number determines the relative speed of every turtle with the other.
```
for turn in range(100):
	ada.forward(randint(1,5))
	bob.forward(randint(1,5))
	cat.forward(randint(1,5))
	dig.forward(randint(1,5))
	elf.forward(randint(1,5))
```
Output will be similar to this.
![alt text](https://github.com/samyuktaprabhu/fun-with-python-for-beginners/blob/master/t2.png)
And that's it- simple and easy.
