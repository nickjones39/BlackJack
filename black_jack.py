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

try:
    from art import logo
except ImportError:
    logo = "====== BLACKJACK ======"


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

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

    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List.
    # If no, then the game has ended.
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
def play_game():
    # Create empty lists for the player's and computer's cards
    user_cards = []
    computer_cards = []

    # Deal two cards to both the player and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Track whether the game is over
    game_over = False

    # Keep playing while the game is not over
    while not game_over:

        # Calculate the current scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show the player's cards and current score
        print(f"Your cards: {user_cards}, current score: {user_score}")

        # Show only the computer's first card
        print(f"Computer's first card: {computer_cards[0]}")

        # End the game if the player or computer has Blackjack,
        # or if the player's score is over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            # Ask the player if they want to draw another card
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            # Deal another card if the player chooses yes
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Let the computer draw cards if the player is still in the game
    if user_score != 0 and user_score <= 21:

        # The computer keeps drawing while the score is below 17
        while computer_score < 17:

            # Deal another card to the computer
            computer_cards.append(deal_card())

            # Recalculate the computer's score
            computer_score = calculate_score(computer_cards)

    # Calculate the final scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Show the final hands and scores
    print(f"\nYour final hand: {user_cards}")
    print(f"Your final score: {user_score}")

    print(f"Computer's final hand: {computer_cards}")
    print(f"Computer's final score: {computer_score}")

    # Compare the final scores and display the result
    result = compare(user_score, computer_score)
    print(result)


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.

# Main program
def main():

    print(logo)

    while True:

        answer = input("Do you want to play Blackjack? (y/n): ")

        if answer == "y":

            play_game()

        elif answer == "n":

            print("Goodbye!")
            break

        else:

            print("Please enter y or n.")


if __name__ == "__main__":
    main()