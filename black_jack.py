############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


import random
from art import logo


def deal_card():
    """Returns a random card from the deck."""

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for a blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Check for an 11 (ace) and replace with 1 if score is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    """Compare user and computer scores to determine the winner."""
    if user_score == computer_score:
        return "PUSH"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():

    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List.
    # If no, then the game has ended.
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
