'''
THIS IS A CODE WRITTEN WITH SPECIFIED OBJECTIVES FROM PYTHON COURSE
'''

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # Suits for regular deck of cards
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')  # Ranks for regular deck of cards
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11} # Values for each rank, special cards has value of 10 in BlackJack, while Aces can be either 1 or 11

import random  # For shuffling the deck later

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  # Assigning the value of the card based on its rank

    def __str__(self):
        return self.rank + ' of ' + self.suit  # String representation of a card


class Deck:

    def __init__(self):
        self.deck = []  # Starting with an empty deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,
                                      rank))  # Creating a Card object for each combination of suit/rank and adding it to the deck

    def __str__(self):
        deck_comp = ''  # Empty string to represent the deck
        for card in self.deck:  # Iterating over each card from the deck
            deck_comp += '\n' + card.__str__()  # Adding a string of the card to the string deck
        return 'The deck has:' + deck_comp  # Returning the deck representation string

    def shuffle(self):
        random.shuffle(self.deck)  # Shuffling the deck

    def deal(self):
        single_card = self.deck.pop()  # Removing and returning the last card from the deck
        return single_card  # Returning the card that was dealt


class Hand:
    def __init__(self):
        self.cards = []  # Empty list to hold the cards in the hand
        self.value = 0  # Initial value of the hand
        self.aces = 0  # Initial count of aces in the hand

    def add_card(self, card):
        self.cards.append(card)  # Adding the drawn card to the hand
        self.value += card.value  # Updating the value of hand with drawn card
        if card.rank == 'Ace':  # Drawing Ace
            self.aces += 1  # Updating the count of aces in the hand
            if self.value > 21 and self.aces == 2:  # Adding a scenario when first two cards are Aces to prevent immediate Bust
                self.value -= 10

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:  # Our value of the hand is greater than 21 with Ace: 11, so we want to count Ace as 1 in this case
            self.value -= 10  # Reducing the value of the hand by 10
            self.aces -= 1  # Decreasing the count of aces from hand


class Chips:

    def __init__(self):
        self.total = 100  # Total of chips
        self.bet = 0  # Initial bet amount

    def win_bet(self):
        self.total += self.bet * 2  # Adding the bet amount to the total of chips when there is a win with Dealer

    def lose_bet(self):
        self.total -= self.bet  # Removing the bet amount from the total of chips when there is a loss with Dealer


def take_bet(chips):
    while True:
        try:
            bet = int(input('Please place your bet: '))  # Player placing bet
            if 0 < bet <= chips.total:  # Checking if the bet is possible
                return bet
            else:
                print('\nInvalid bet. Please enter a bet within your available chips.')
        except ValueError:  # Preventing the game to give error when player places incorrect bet (not integer)
            print('\nInvalid input. Please enter a valid integer.')


def hit(deck, hand):
    hand.add_card(deck.deal())  # Adding a card to the player/dealer hand from the deck
    hand.adjust_for_ace()  # Adjusting the value of the hand to account for aces


def hit_or_stand(deck, hand):
    global playing  # Global variable controling the while loop
    while True:
        choice = input("\nWould you like to hit or stand? Enter 'h' or 's': ")
        if choice == 'h':  # Hit
            hit(deck, hand)  # Calling the hit() function if player wants to hit
        elif choice == 's':  # Stand
            print("\nPlayer stand. Dealer's turn.")
            playing = False  # Ending Player's turn
        else:
            print("\nInvalid input. Please enter 'h' for hit or 's' for stand.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")  # Hiding a card of the Dealer's hand
    print("", dealer.cards[1])  # Showing the second card of the Dealer's hand
    print("\nPlayer's Hand:", *player.cards, sep='\n ')  # * is unpacking operator, sep is separator


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')  # Showing Dealer's hand
    print("Dealer's Value =", dealer.value)  # Showind Dealer's value
    print("\nPlayer's Hand:", *player.cards, sep='\n ')  # Showing Player's hand
    print("Player's Value:", player.value)  # Showing Player's value


def player_busts(player, dealer, chips):
    print('\nPlayer busts! Dealer wins this bet!')  # Player has busted
    chips.lose_bet()  # Removing the player's bet from their total chips


def player_wins(player, dealer, chips):
    print('\nPlayer wins this bet!')  # Player wins the bet
    chips.win_bet()  # Adding the player's bet to their total chips


def dealer_busts(player, dealer, chips):
    print('\nDealer busts! Player wins this bet!')  # Dealer has busted
    chips.win_bet()  # Adding the player's bet to their total chips


def dealer_wins(player, dealer, chips):
    print('\nDealer wins this bet!')
    chips.lose_bet()  # Removing the player's bet from their total chips


def push(player, dealer):
    print('\nGame tied! Push.')  # Tie, Player doesn't win or lose any chips in this case


player_chips = Chips()

# GAME LOOP
while True:
    print("\nWelcome to BlackJack!\n")

    deck = Deck()  # Creating a deck of cards
    deck.shuffle()  # Shuffling the deck

    player_hand = Hand()
    dealer_hand = Hand()

    for x in range(2):
        player_hand.add_card(deck.deal())  # Dealing two cards to the Player's hand
        dealer_hand.add_card(deck.deal())  # Dealing two cards to the Dealer's hand

    player_chips = Chips()  # Defining Player's chips

    take_bet(player_chips)  # Taking Player's bet

    show_some(player_hand, dealer_hand)  # Showing initial cards

    while playing:  # Player is playing

        hit_or_stand(deck, player_hand)  # Asking if player wants to hit or stand
        show_some(player_hand, dealer_hand)  # Keeping one dealer's card hidden

        if player_hand.value > 21:  # Checking if player's hand value is more than 21
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:  # Player hasn't busted
        while dealer_hand.value < 17:  # Dealer plays until reaches 17
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)  # Showing all cards

        if dealer_hand.value > 21:  # Dealer busted
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:  # Dealer has more value than Player
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:  # Player has more value than Dealer
            player_wins(player_hand, dealer_hand, player_chips)

        else:  # Push
            push(player_hand, dealer_hand)

    print("\nPlayer's won chips: ", player_chips.total)  # Chips balance

    play_again = input("\nDo you want to play again? Enter 'yes' or 'no': ")  # Asking to play again
    if play_again.lower() == 'yes':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break  # Exiting the game loop if Player doesn't want to play again
