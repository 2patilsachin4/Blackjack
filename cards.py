##Cards Module
RANKS = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
SUITS = ['c','s','d','h']
import random

class Card(object):
    """ A playing card"""
    RANKS = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
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
            rep = "<empty"
            return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        if type(card) == Card:
            self.cards.append(card)
        else:
            return "This is not a valid Card"

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

if __name__ == "__main__":
    print "This is a module with classes for playing cards."
    raw_input("\n\nPress the enter key to exit.")
    
            
        
            
