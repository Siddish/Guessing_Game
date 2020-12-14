import random

def user_guess():
	comp_g = random.randint(1,20)
	user_guess = 0
	while comp_g != user_guess:
		user_guess = int(input("Enter a number between 1 and 20: "))
		if user_guess > comp_g:
			print("Too high. Guess again")
		elif user_guess < comp_g:
			print("Too low. Guess again")
	print("Yay! You guessed the number correctly.")


def computer_g():
	c_guess = 0
	low = 1
	high = 20
	usr_reply = ''
	print("Did you think of the number between 1 and 20 that you want the computer to guess?")
	cont = input("Input y(yes)when you are ready\n")
	if cont == 'y':
		while usr_reply != 'c':
			if low != high:
				c_guess = random.randint(low,high)
			else:
				c_guess = low
			usr_reply = input(f"Is {c_guess} the number? Enter low(l), high(h) or c(correct)".lower())
			if usr_reply == 'h':
				high = c_guess
			elif usr_reply == 'l':
				low = c_guess
	print("The computer guessed it right")

print("Do you want the computer to guess or do you want to guess?\n")
usr = input("Enter c(computer) or u(you): ")
if usr == 'c':
	computer_g()
else:
	user_guess()