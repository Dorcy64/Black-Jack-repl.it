import random
from replit import clear
from art import logo

def black_jack():
	
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	human_cards = []
	human_cards.append(random.choice(cards))
	human_cards.append(random.choice(cards))

	computer_cards = []
	computer_cards.append(random.choice(cards))


	def human():
		while 21 > sum(human_cards):
			print(f"	Your cards are {human_cards}, current score: {sum(human_cards)}")
			print(f"	Computer cards are {computer_cards[0]}")
			repeat = 0
			while 1 > repeat:
				go_gain = input("Type 'y' to get another card, type 'n' to pass: ")
				if go_gain == "n":
					repeat += 1
					break
				elif go_gain == "y":
					break
			if go_gain == "y":
				human_cards.append(random.choice(cards))
			else :
				break

	human()
	
	human_final_score = sum(human_cards)

	if human_final_score > 21:
		print(f"You lose\nFinal cards {human_cards} final score: {human_final_score}, you went over 21")
		return "loss"
	elif human_final_score == 21 and len(human_cards) == 2:
		print(f"Black Jack you won with {human_cards}, final score: 21")
		return "win"
	else:
		def computer():
			while 21 > sum(computer_cards):
				new_card2 = random.choice(cards)
				if (sum(computer_cards) + new_card2) > 21 :
					break
				else :
					computer_cards.append(new_card2)

		
		computer()


		human_final_score = sum(human_cards)
		computer_final_score = sum(computer_cards)

		print(f"	Your cards are {human_cards}, current score: {human_final_score}")
		print(f"	Computers final cards are {computer_cards} and the score is {computer_final_score}")

		if sum(computer_cards) == 21 and sum(human_cards) != 21:
			print("You lose")
			return "loss"
		human_score_winner = 21 - human_final_score
		copmuter_score_to_win = 21 - computer_final_score

		
		if human_score_winner == copmuter_score_to_win:
			print("Draw")
			return "draw"
		elif human_score_winner > copmuter_score_to_win:
			print("You lose")
			return "loss"
		elif copmuter_score_to_win > human_score_winner:
			print("You win")
			return "win"
			
current_balance = 2500

while current_balance > 0:
	clear()
	print(logo)

	bet = int(input(f"Your current balance is {current_balance}, how much do you want to bet? $"))

	scenario = black_jack()

	print("\n", end = "")

	if scenario == "loss":
		current_balance -= bet
	elif scenario == "win":
		current_balance += bet

	print(f"Your current balance is {current_balance}")
	press_enter = input("\nPress Enter or Return to Continue: ")

	if current_balance <= 0:
		play_again_num = 0
		while 1 > play_again_num: 
			play_again_q = input("\nDo you want to play again? y / n : ")
			if play_again_q == "y":
				play_again_num += 1
				current_balance = 2500
			elif play_again_q == "n":
				play_again_num += 1
				current_balance = 0

