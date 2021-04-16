
import random
import os
os.system("cls")

shapes = ["hearts", "diamonds", "spades", "clubs"]
numbers = [i for i in range(2,11)]
numbers += ["Jack", "Queen", "King", "Ace"]
cards = []
for shape in shapes:
    for number in numbers:
        cards.append([number, shape])
        

temp_cards = list(cards)

class player:
    def __init__(self):
        self.hand = []
        self.get_card()
        self.get_card()
    def get_card(self):
        global temp_cards
        card = random.choice(temp_cards)
        self.hand.append(card)
        temp_cards.remove(card)
    def card_sum(self):
        _sum = 0
        for card in self.hand:
            if isinstance(card[0], int):
                _sum += card[0]
            elif card[0] == "Ace":
                if _sum + 11 > 21:
                    _sum += 1
                else:
                    _sum += 11
            else:
                _sum += 10
        return _sum




game = True
is_round = True
try:
    while game:
        while is_round:
            user = player()
            bot = player()

            won = False
            lost = False
            tie = False
            stand = False

            print(f"You:{user.hand, user.card_sum()}")
            print(f"Bot:{bot.hand, bot.card_sum()}")

            if user.card_sum() == 21:
                won = True
            if bot.card_sum() == 21:
                lost = True
            if lost and won:
                tie = True
            while not won and not lost and not stand :
                while True:
                    play = input("H/S: ").lower().strip()
                    if play == "s" or play == "h":
                        break
                if play == "s":
                    stand = True
                    break
                user.get_card()
                if user.card_sum() > 21:
                    lost = True
                if user.card_sum() == 21:
                    won = True
                if len(user.hand) == 5:
                    won = True
                os.system("cls")
                print(f"You:{user.hand, user.card_sum()}")
                print(f"Bot:{bot.hand, bot.card_sum()}")

            if not lost and not won:
                while bot.card_sum() < 17 or user.card_sum() > bot.card_sum():
                    if bot.card_sum() > user.card_sum():
                        lost = True
                        break
                    bot.get_card()
                    if bot.card_sum() == 21:
                        lost = True
                    if bot.card_sum() > 21:
                        won = True
            os.system("cls")
            print(f"You:{user.hand, user.card_sum()}")
            print(f"Bot:{bot.hand, bot.card_sum()}")

            if user.card_sum() > bot.card_sum() and user.card_sum() < 22:
                won = True
            if user.card_sum() == bot.card_sum() and user.card_sum() < 22:
                tie = True
            if user.card_sum() < bot.card_sum() and bot.card_sum() < 22:
                lost = True
            
            if lost:
                print("You lost")
            if tie:
                print("You tied")
            if won:
                print("You won")

            another_round = input("another round: ")
            os.system("cls")
            temp_cards = cards.copy()
            if another_round == "n":
                os.system("cls")
                break
except KeyboardInterrupt:
    os.system("cls")