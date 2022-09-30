import random
from replit import clear

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
        return "Draw"
    elif computer_score == 0:
        return "Lose, dealer has blackjack"
    elif user_score == 0:
        return "Win with blackjack"
    elif user_score > 21:
        return "Lose. You went over"
    elif computer_score > 21:
        return "Win. Dealer went over"
    elif computer_score > user_score:
        return "Lose"
    elif user_score > computer_score:
        return "Win"

end_game = False
while not end_game:
    play = input("Wannna play Blackjack? Y/N ").lower()
    if play == 'y':
        user_cards = []
        computer_cards = []
        
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        stop_drawing = False
        while not stop_drawing:
            clear()
            print("---Starting game---")
            
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"""Your cards: {user_cards}, current score: {user_score}
Computer's first card: {computer_cards[0]}""")
            
            if user_score == 0 or computer_score == 0 or user_score > 21:
                stop_drawing = True
            else:
                draw_another = input("Type 'y' to hit, type 'n' to pass: ").lower()
                if draw_another == 'y':
                    user_cards.append(deal_card())
                else:
                    stop_drawing = True
            
        while sum(computer_cards) < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        clear()
        
        print(f"""Your final hand: {user_cards}, final score: {user_score}
Computer's final hand: {computer_cards}, final score: {computer_score}\n""")
        print(compare(user_score, computer_score))
        print("---")
    else:
        end_game = True
        print("---Exiting game---")