import random
import time
from replit import clear
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "\33[33mDRAW\33[0m"
    elif computer_score == 0:
        return "\33[31mLOSE\nDealer has Blackjack\33[0m"
    elif user_score == 0:
        return "\33[32mWIN\nBlackjack\33[0m"
    elif user_score > 21:
        return "\33[31mLOSE\nYou went over\33[0m"
    elif computer_score > 21:
        return "\33[32mWIN\nDealer went over\33[0m"
    elif computer_score > user_score:
        return "\33[31mLOSE\33[0m"
    elif user_score > computer_score:
        return "\33[32mWIN\33[0m"

play = input("Psst. Hey. Wannna play a \33[1mgame\33[0m?\n\33[32mY\33[0m/\33[31mN\33[0m ").lower()

end_game = False
while not end_game:
    if play == 'y':
        logo()
        user_cards = []
        computer_cards = []
        
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        clear()
        logo()
        print("\33[32mStarting game.\33[0m")
        time.sleep(0.5)
        clear()
        logo()
        print("\33[32mStarting game..\33[0m")
        time.sleep(0.5)
        clear()
        logo()
        print("\33[32mStarting game...\33[0m")
        time.sleep(0.5)
        clear()
        logo()
        
        stop_drawing = False
        while not stop_drawing:
            clear()
            logo()
            
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"""Your cards: \33[34m{user_cards}\33[0m, current score: \33[34m{user_score}\33[0m
Computer's first card: \33[35m{computer_cards[0]}\33[0m""")
            
            if user_score == 0 or computer_score == 0 or user_score > 21:
                stop_drawing = True
            else:
                draw_another = input("\nType 'y' to hit, type 'n' to pass: ").lower()
                if draw_another == 'y':
                    user_cards.append(deal_card())
                else:
                    stop_drawing = True
            
        while sum(computer_cards) < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        clear()
        logo()
        
        print(f"""Your final hand: \33[34m{user_cards}\33[0m, final score: \33[34m{user_score}\33[0m
Computer's final hand: \33[35m{computer_cards}\33[0m, final score: \33[35m{computer_score}\33[0m\n""")
        print(compare(user_score, computer_score))
        time.sleep(1.5)
        play = input("\nPsst. Wannna play again?\n\33[32mY\33[0m/\33[31mN\33[0m ").lower()

    else:
        end_game = True
        clear()
        logo()
        print("\33[31mExiting game.\33[0m")
        time.sleep(0.5)
        clear()
        logo()
        print("\33[31mExiting game..\33[0m")
        time.sleep(0.5)
        clear()
        logo()
        print("\33[31mExiting game...\33[0m")
        time.sleep(0.5)
        clear()