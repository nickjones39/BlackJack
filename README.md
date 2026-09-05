# BlackJack

A Python console implementation of the card game Blackjack, built as part of the
MSE800 Week 6 Version Control activity. The game logic itself comes from an
earlier course exercise; this repository exists to practice publishing a
project to a remote Git repository using the distributed version control
workflow covered in the Week 6 slides (`Version Control(2).pptx`).

## House Rules

- The deck is unlimited in size.
- There are no jokers.
- Jack, Queen and King all count as 10.
- The Ace can count as 11 or 1.
- The deck is represented by the list `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`.
- All cards have an equal probability of being drawn.
- Cards are not removed from the deck once drawn (the deck is effectively infinite).

## How to Play

1. Run `black_jack.py` with Python 3.
2. Type `y` when prompted to start a round of Blackjack.
3. You and the computer are each dealt two cards.
4. Choose whether to draw another card ("hit") or stop ("stand").
5. The computer draws automatically while its score is below 17.
6. A hand of exactly Ace + 10 (21 with two cards) is a Blackjack and beats a
   regular 21.
7. Whoever has the higher score without going over 21 wins; going over 21 is a
   bust and an automatic loss.
8. After a round ends you can choose to play again.

## Requirements

- Python 3
- The `art` module (used to display the game's ASCII logo)

## Version Control

This project is tracked with Git and hosted on GitHub as a public repository,
following the distributed version control workflow (local commit → push to
remote) introduced in the Week 6 Version Control lecture.
