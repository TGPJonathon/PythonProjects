import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        if self.aces > 0 and self.value > 21:
            self.value -= 10
        self.aces = 0
    
    def __str__(self):
        deck_comp = ''
        for card in self.cards:
            deck_comp += '\n ' + card.__str__()
        return 'The hand has: ' + deck_comp

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chip):
    while True:
        try:
            chip.bet = int(input("Place a bet "))
        except:
            print("Enter a number")
        else:
            if(chip.bet > chip.total):
                print("You don't have enough to cover that bet")
            else:
                print(f"{chip.bet} is the bet amount")
                break

def hit(deck, hand):
    hand.adjust_for_ace()
    hand.add_card(deck.deal())

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        choice = input("Would you like to Hit or Stand? ").capitalize()
        if choice == "Hit":
            hit(deck, hand)
        elif choice == "Stand":
            playing = False
        else:
            print("Try again")
            continue
        break

def show_some(player, dealer):
    print(f"Player cards:\n", *player.cards)
    print(f"Dealer cards:\n {dealer.cards[1]}")
    

def show_all(player,dealer):
    print(f"Player cards:\n", *player.cards)
    print(f"\n Player Value {player.value}")
    print(f"Dealer cards:\n", *dealer.cards)
    print(f"\n Dealer Value {dealer.value}")

def player_busts(player_hand, chips):
    print("Player busts")
    chips.lose_bet()
    
def player_wins(player_hand, chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(dealer,chips):
    print("Dealer busts")
    chips.win_bet()
    
def dealer_wins(dealer,chips):
    print("Dealer wins")
    chips.lose_bet()
    
def push():
    print("There's a Tie")

'''
The Actual Game
'''

while True:
    # Print an opening statement
    print("Welcome to our Blackjack game")

    
    # Create & shuffle the deck, deal two cards to each player
    play_deck = Deck()
    play_deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(play_deck.deal())
    player_hand.add_card(play_deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(play_deck.deal())
    dealer_hand.add_card(play_deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips()
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(play_deck,player_hand)
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, player_chips)
            break
            
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            dealer_hand.add_card(play_deck.deal())
    
        # Show all cards
        show_all(player_hand, dealer_hand)
    
        # Run different winning scenarios
        if(dealer_hand.value > 21):
            dealer_busts(dealer_hand, player_chips)
        elif(player_hand.value > dealer_hand.value):
            player_wins(player_hand, player_chips)
        elif(player_hand.value < dealer_hand.value):
            dealer_wins(player_hand, player_chips)
        elif(player_hand.value == dealer_hand.value):
            push()
    
        
    
    # Inform Player of their chips total
    print(f"Your total number of chips: {player_chips.total}")
    
    # Ask to play again
    play_again = int(input("Would you like to play again? 1 Yes, 2 No"))
    if(play_again == 1):
        play_again = True
        playing = True
    else:
          play_again = False
          
    if(play_again):
          print("Lets play again")
    else:
          print("Thanks for playing")
          break








    