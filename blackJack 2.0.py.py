import random


class Blackjack:
    def __init__(self):
        self.player_name = input("Welcome to Nexus BlackJack, please enter your name: ")
        self.suits = {"♣": 0, "♦": 1, "♠": 2, "♥": 3}
        self.card_numbers = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "Jack": 10,
                             "Queen": 10, "King": 10}
        self.player_cards = []
        self.dealer_cards = []
        self.player_score = 0
        self.dealer_score = 0

    def deal_card(self, cards):
        suit = random.choice(list(self.suits.keys()))
        number = random.choice(list(self.card_numbers.keys()))
        cards.append(f"{number} of {suit}")
        return number

    def calculate_score(self, cards):
        score = sum([self.card_numbers[card.split(" of ")[0]] for card in cards])
        if score > 21 and any("Ace" in card for card in cards):
            score -= 10
        return score

    def gameplay(self):
        self.player_score += self.calculate_score([self.deal_card(self.player_cards) for _ in range(2)])
        print(f"\nOk, {self.player_name} you have the next hand: " + " and ".join(self.player_cards))
        self.dealer_score += self.calculate_score([self.deal_card(self.dealer_cards) for _ in range(2)])
        # Show one of the dealer's cards
        print(f"And one of the dealer's card is: {self.dealer_cards[0]}")
        print(f"Your current score is: {self.player_score}\nDealer's score is: {self.card_numbers[self.dealer_cards[0].split(' of ')[0]]}")
        if self.dealer_score == 21:
            print(f"Sorry, you have lost. Dealer's cards are: {' and '.join(self.dealer_cards)}")
            return
        elif self.player_score == 21:
            print(f"\nCongratulations, you've won!!!")
            return

        while True:
            question = input("Do you want to Hit or Stand? ").lower()
            if question == "hit":
                self.player_score += self.calculate_score([self.deal_card(self.player_cards)])
                print(f"Your hand is now: {' and '.join(self.player_cards)}")
                print(f"Your score is now: {self.player_score}")
                if self.player_score > 21:
                    print(f"Sorry, you went over 21. You lost. Dealer's cards were: {' and '.join(self.dealer_cards)}")
                    return

                """TREBUIE ADAUGATA SI VARIANTA IN CARE ARE SCORU 21 DUPA PRIMU HIT"""

            elif question == "stand":
                print(f"You have chosen to stand. Your final score is {self.player_score}")
                while self.dealer_score < 17:
                    self.dealer_score += self.calculate_score([self.deal_card(self.dealer_cards)])
                    print(f"Dealer's score is now: {self.dealer_score}")
                    if self.dealer_score > 21:
                        print(f"Dealer went over 21. You won! Dealer's cards were: {' and '.join(self.dealer_cards)}")
                        return
                if self.dealer_score > self.player_score:
                    print(f"Dealer wins with a score of {self.dealer_score}. Dealer's cards were: {' and '.join(self.dealer_cards)}")
                elif self.dealer_score == self.player_score:
                    print(f"It's a tie! Dealer's cards were: {' and '.join(self.dealer_cards)}")
                else:
                    print(f"You win with a score of {self.player_score}! Dealer's cards were: {' and '.join(self.dealer_cards)}")
                return
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

game = Blackjack()
game.gameplay()