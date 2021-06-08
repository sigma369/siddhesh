# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
dealer_score = 0
your_score = 0
result = ""
score_bug_fix = True

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    global card_images
    
    def __init__(self):
        self.hand_list = []	# create Hand object
        
    def hand_list(self):
        return self.hand_list

    def __str__(self): # return a string representation of a hand
        
        dummy_string = 'Hand contains '
        for card in self.hand_list:	
            dummy_string += str(card.get_suit()) + str(card.get_rank()) + ' '
        return dummy_string  
               
    def add_card(self, card):
        self.hand_list.append(card)	# add a card object to a hand

    def get_value(self):
        self.value = 0
#        print len(self.hand_list)
        
        for card in self.hand_list:
            self.value += VALUES[str(card.get_rank())]
            
        for card in self.hand_list:
            if card.get_rank() == 'A' and (self.value + 10) > 21 :
                return self.value
            elif card.get_rank() == 'A' and (self.value + 10) <= 21:
                self.value += 10
                return self.value 

        return self.value
   
    def draw(self, canvas, pos):
        
        for i in range(0,len(self.hand_list)):
           if in_play == True and first_dealer_card == self.hand_list[i]:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
           else:
                self.hand_list[i].draw(canvas,[(pos[0] + 82*i), pos[1]])

                    
       

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
             

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return random.choice(self.deck)	# deal a card object from the deck
    
    def __str__(self):
        dummy_string = 'Deck contains '
        for card in self.deck:	
            dummy_string += str(card.get_suit()) + str(card.get_rank()) + ' '
        return dummy_string  	# return a string representing the deck        




#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, match_deck, outcome, first_dealer_card, result
    global score_bug_fix
    score_bug_fix = True
    in_play = True
    outcome = "Hit or stand?"
    result =""
    
    # creating the global deck and shuffle
    match_deck = Deck()
    match_deck.shuffle()
    print match_deck
    # Creating Global hands for dealer and player
    player_hand = Hand()
    dealer_hand = Hand()    	
    
    # Assign two cards to each player and dealer
    for i in range(0,2):
        player_hand.add_card(match_deck.deal_card())
        dealer_hand.add_card(match_deck.deal_card())
        
    # Checking if same cards in deck or not
    while dealer_hand.hand_list[0] == dealer_hand.hand_list[1] or player_hand.hand_list[0] == player_hand.hand_list[1] or dealer_hand.hand_list[0] == player_hand.hand_list[0] or dealer_hand.hand_list[0] == player_hand.hand_list[1] or dealer_hand.hand_list[1] == player_hand.hand_list[0] or dealer_hand.hand_list[1] == player_hand.hand_list[1]:																		
        player_hand = Hand()
        dealer_hand = Hand()
        for i in range(0,2):
        
            player_hand.add_card(match_deck.deal_card())
            dealer_hand.add_card(match_deck.deal_card())
#            
    # saving 1st dealer card to hide
    first_dealer_card = dealer_hand.hand_list[0]
    
    print 'Dealer {0} and Player{1}'.format(dealer_hand, player_hand)
    print 'Dealer score is {0} and Your score is {1}'.format(dealer_hand.get_value(), player_hand.get_value()) 
    
def hit():
    global outcome, in_play, result
    global dealer_score, your_score, score_bug_fix
    
    if in_play and player_hand.get_value() <= 21:
        dummy_card = Card(random.choice(SUITS), random.choice(RANKS))
        dummy_card = match_deck.deal_card()
        
        while (dummy_card in dealer_hand.hand_list):
            dummy_card = Card(random.choice(SUITS), random.choice(RANKS))
            dummy_card = match_deck.deal_card()            
        
        player_hand.add_card(dummy_card)
        
    
    if in_play and player_hand.get_value() > 21:
        print 'You are busted and dealer won'
        result = 'You are busted and dealer won'
        if score_bug_fix:
            dealer_score += 1
        score_bug_fix = False
        outcome = "New deal?"
        
    print 'Dealer {0} and Player {1}'.format(dealer_hand, player_hand)
    print 'Dealer score is {0} and Your score is {1}'.format(dealer_hand.get_value(), player_hand.get_value()) 
               
def Stand():
    global in_play, outcome, result
    global dealer_score, your_score, score_bug_fix 
    
#    print 'working'
    in_play = False
    
    if player_hand.get_value() > 21:
        in_play = True
    
    if in_play and player_hand.get_value() > 21:
        print 'You are busted and dealer won'
    
    check = bool(in_play)
    
    while check == False and player_hand.get_value() <= 21:
        
        if dealer_hand.get_value() < 17:
            print dealer_hand.get_value()
            dealer_hand.add_card(match_deck.deal_card())
        else:
            check = True    
     
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    # assign a message to outcome, update in_play and score
    if dealer_hand.get_value() <= 21 and dealer_hand.get_value() >= player_hand.get_value() and player_hand.get_value() <= 21 and score_bug_fix:
        print 'You lost and dealer won'
        result = 'You lost and dealer won'
        dealer_score += 1 
        score_bug_fix = False
        
        print 'Dealer score is {0} and Your score is {1}'.format(dealer_hand.get_value(), player_hand.get_value()) 
        print 'Dealer {0} and Player {1}'.format(dealer_hand, player_hand)
        outcome = "New deal?"
        
    elif dealer_hand.get_value() <= 21 and dealer_hand.get_value() <= player_hand.get_value() and player_hand.get_value() <= 21 and score_bug_fix:
        print 'You won and dealer lost'
        result = 'You won and dealer lost'
        your_score += 1
        score_bug_fix = False
        
        print 'Dealer score is {0} and Your score is {1}'.format(dealer_hand.get_value(), player_hand.get_value()) 
        print 'Dealer {0} and Player {1}'.format(dealer_hand, player_hand)
        outcome = "New deal?"
        
    elif dealer_hand.get_value() > 21 and player_hand.get_value() <= 21 and score_bug_fix:
        print 'You won and dealer busted'
        result = 'You won and dealer busted'
        your_score += 1
        score_bug_fix = False
        
        print 'Dealer score is {0} and Your score is {1}'.format(dealer_hand.get_value(), player_hand.get_value()) 
        print 'Dealer {0} and Player {1}'.format(dealer_hand, player_hand)
        outcome = "New deal?"
    
    
# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas,[10, 200])
    player_hand.draw(canvas,[10, 400])
    
#    print in_play
    canvas.draw_text(outcome , (250, 380), 24, 'Black')
    canvas.draw_text('Your Hand' , (50, 380), 24, 'Black')
    canvas.draw_text("Dealer's Hand" , (50, 180), 24, 'Black')
    canvas.draw_text("Blackjack" , (50, 100), 50, 'Black')
    
    # Printing the individual score
    canvas.draw_text('Your Score is {0}'.format(your_score) , (350, 100), 26, 'Black')
    canvas.draw_text("Dealer's Score is {0}".format(dealer_score) , (350, 150), 26, 'Black')
    
    #printing result
    canvas.draw_text(result , (250, 400), 24, 'Black')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", Stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
#test_deck = Deck()
#test_hand = Hand()
#print test_deck
#print test_deck.shuffle()

# remember to review the gradic rubric