#Blackjack Game.

#-----------------------------------------------------------------------------
##Cards Module
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
SUITS = ['c','s','d','h']
import random

class Card(object):
    """ A playing card"""
    RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    SUITS = ['c','s','d','h']
    def __init__(self,rank,suit,face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = ''
            rep += self.rank + self.suit
            return rep

        else:
            rep = 'XX'
            return rep

    def flip(self):
        self.is_face_up = not self.is_face_up



class Hand(object):
    """A hand of playing cards"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
            return rep
        else:
            rep = "<empty>"
            return rep

    def clear(self):
        self.cards = []

    def add(self,card):
            self.cards.append(card)


    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        

class Deck(Hand):
    """A deck of playing cards"""
    def populate(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.add(Card(rank,suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,hands,per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    return "No more cards left to deal"
#--------------------------------------------------------------------------------
#Games module

def ask_yes_no(question):
        """Ask a yes or no question"""
        response = None
        while response in ("y","n"):
            response = raw_input(question).lower()
            return response

def ask_number(question,low,high):
        """Ask for a number within a range"""
        response = None
        while response not in range(low,high):
            response = int(raw_input(question))
            return response
            
#--------------------------------------------------------------------------------        
            


#Blackjack Game

ACE_VALUE = 1

class BJ_Card(Card):
    """A Blackjack Card"""
    def get_value(self):
        if self.is_face_up:
            value = BJ_Card.RANKS.index(self.rank) + 1
            return value
        else:
            value = None
            return value

class BJ_Deck(Deck):
    """A Bkajack Deck."""
    def populate(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(BJ_Card(rank,suit))


class BJ_Hand(Hand):
    """A Blackjack Hand."""
    def __init__(self,name):
        super(BJ_Hand,self).__init__()
        self.name = name

    def total(self):
        total_val = 0
        contains_ace = False
        for card in self.cards:
            if card.get_value():
                total_val += card.get_value()
            if card.get_value() == ACE_VALUE:
                contains_ace = True
        if contains_ace and total_val <=11 and total_val > 0:
            total_val += 10
        return total_val

    def __str__(self):
        rep = ""
        rep += self.name + "\t" + super(BJ_Hand,self).__str__()
        rep += "(" + str(self.total()) + ")"
        return rep
    
    def is_busted(self):
        if self.total() > 21:
            return True
        return False

class BJ_Player(BJ_Hand):
    """ A Blackjack Player"""
    def is_hitting(self):
        response = ""
        response = raw_input("\n" + self.name + ",do you want a hit? (y/n): ")
        return response == "y"

    def bust(self):
        print self.name, "busts."
        self.lose()
        
    def lose(self):
        print self.name, "looses."

    def win(self):
        print self.name, "wins."

    def push(self):
        print self.name, "pushes."


class BJ_Dealer(BJ_Hand):
    """A Blackjack Dealer"""
    def is_hitting(self):
        return self.total() < 17

    def bust(self):
        print self.name, "busts."

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """A Blackjack Game"""
    def __init__(self,names):
        self.players = [] 
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.Deck = BJ_Deck()
        self.Deck.populate()
        self.Deck.shuffle()
        

    def get_still_playing(self):
        remaining = []
        for player in self.players:
            if not player.is_busted():
                remaining.append(player)
        return remaining


    def additional_cards(self,player):
        while not player.is_busted() and player.is_hitting():
            self.Deck.deal([player])
            print player
            if player.is_busted():
                player.bust()
        


    def play(self):
        #deal each player and dealer initially two cards
        self.Deck.deal(self.players + [self.dealer],per_hand = 2)
        
        #Flip dealer's first card to hide its value
        self.dealer.flip_first_card()

        #Display all hands
        for each in self.players:
            print each
        print self.dealer

        #Give each player cards as long as the player requests and hasn't been busted
        for each in self.players:
            self.additional_cards(each)

        self.dealer.flip_first_card()

        #If all players busted,flip dealers first card and print dealer's hand
        remaining = self.get_still_playing()
        if not remaining:
            print self.dealer

           

        #Otherwise play continnues Dealer gets cards as long as the dealer's hand total is less than 17.
        self.additional_cards(self.dealer)
 
        #if dealer busts, all remaining player wins
        if self.dealer.is_busted():
            for each in remaining:
                each.win()

        #Otherwise each reaming player's hand compared with dealer's.
        else:
            for player in remaining:
                if player.total() > self.dealer.total(): 
                    player.win()
                if each.total() < self.dealer.total():
                    player.lose()
                else:
                    player.push()
                                                   

        #Empty the players list for the new game and also the dealer.
        for each in self.players:
            each.clear()
        self.dealer.clear()

#---------------------------------------------------------------------------------


def main():
    print "\t\tWelcome to Blackjack!\n"
    names = []
    number = ask_number("How many players?(1-7): ",low = 1 , high = 8)
    for i in range(number):
        name = raw_input("Enter your name: ")
        names.append(name)

    game = BJ_Game(names)

    again = None
    while again!= "n":
        game.play()
        again = raw_input("\nDo you want to play again?: ")

main()
raw_input("\n\nPress the enter key to exit.")


    
            
    

