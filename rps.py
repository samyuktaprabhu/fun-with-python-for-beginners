#!/bin/python3
print("Welcome to the game of rock paper scissor")
print("In this game you will play against the computer.")

print("Rules: You and the computer both choose rock, paper or scissors. The winner is decided by these rules:\nRock blunts scissors\nPaper covers rock\nScissors cut paper")

from random import randint #importing randint function from random package
name=raw_input("Hey there !What's your name?")
count,chance,comp,player=0,1,0,0

while comp<5 and player<5:

	you=raw_input("What do you choose {} ? Rock(r), Paper(p) or scissor(s)?".format(name))

	print("Cool!!! You chose {}".format(you))

	print("It is the computers turn now")
	choice=randint(1,3)
	
	if choice==1:
		com='r'
	elif choice==2:
		com='p'
	else:
		com='s'
	print("The computer played {} !".format(com))

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
		print("{} , you win!".format(name))
		player+=1
	elif you=='s' and com=='r':
		print("Oh ! The computer won")
		comp+=1
	else:
		print("Error occurred,play again")
	
if comp==5:
	print("OVERALL CHAMPION : Computer ! :/ ")
else:
	print("OVERALL CHAMPION : {} ! *_* ".format(name))

#End of code
	
	
