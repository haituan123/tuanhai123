print("Player can choose paper, scissor or rock")

from random import randint
player= input()
computer= randint(1,3)


if computer == 1:
	computer = "paper"
if computer == 2:
	computer = "rock"
if computer == 3:
	computer = "scissor"

print("------------")
print("Player choose:"+ player)
print("computer chooses: "+ str(computer))
print("------------")
if player == computer:
	print("Draw")
else:
	if player == "scissor":
		if computer == "paper":
			print("Win")
		else:
			print("Lose")

	elif player == "paper":
		if computer == "scissor":
			print("Lose")
		else:
			print("Win")

	elif player == "rock":
		if computer == "scissor":
			print("Win")
		else:
			print("Lose")
	else:
		print("choose again")
	

