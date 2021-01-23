import random,sys

print("Welcome to Rock Paper Scissors Game!!!")

player = 0
computer = 0

while True:
	print(f"""Player scores = {player}
Computer scores = {computer}""")
	while True:
		print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
		playerMove=input()
		if playerMove=='q':
			sys.exit()
		if playerMove=='r' or playerMove=='p' or playerMove=='s':
			break
		print('Type one of r, p, s, q')
	if playerMove=='r':
		print('Rock versus...')
	elif playerMove=='p':
		print('Paper versus...')
	elif playerMove=='s':
		print('Scissors versus...')

	computerChoice = ['r','p','s']

	computerMove = random.choice(computerChoice)
	print(computerMove)

	if computerMove=='r' and playerMove == 'p':
		player+=1
	elif computerMove == 'p' and playerMove == 'r':
		computer+=1
	elif computerMove == 'r' and playerMove == 's':
		computer+=1
	elif computerMove == 's' and playerMove == 'r':
		player+=1
	elif computerMove == 'p' and playerMove == 's':
		player+=1
	elif computerMove == 's' and playerMove == 'p':
		computer+=1

	if player == 5:
		print(f'Player wins\nPlayer\'s score is: {player}\nComputer\'s score is: {computer}')
		player,computer = 0,0
	if computer == 5:
		print('Computer wins')
		player,computer = 0,0


