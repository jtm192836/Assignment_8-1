#!/usr/bin/python3
print("Welcome to the Game!")
def drawsmall():
	a = (' ___' *  3 )
	b = '   '.join('||||')
	print('\n'.join((a, b, a, b, a, b, a, )))

drawsmall()
list1 =[0,0,0,
	0,0,0,
	0,0,0]
print(list1)
print("Player 1's chance")
pos,num=input("Enter the position and number to be entered:").split(",")

print("Player 2's chance")
pos,num=input("Enter the position and number to be entered:").split(",")


