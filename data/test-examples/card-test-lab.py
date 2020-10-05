import unittest

from cards import Hand, Card, Deck

class TestDeck(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()
        
    def test52(self):
        self.assertEqual(len(self.deck), 52)
        
    def test_no_dupes(self):
        seen = set()
        for card in self.deck:
            self.assertNotIn(card, seen)
            seen.add(card)
            
    def test_no_dupes2(self):
        self.assertEqual(
            len(set(self.deck)), 
            len(self.deck),
        )
            
class TestCards(unittest.TestCase):
    
    def test_same_card(self):
        c0 = Card(rank='A', suit='clubs')
        c1 = Card(rank='A', suit='clubs')
        self.assertEqual(c0, c1)
        

    def test_different_card(self):
        c0 = Card(rank='A', suit='clubs')
        c1 = Card(rank='K', suit='clubs')
        self.assertNotEqual(c0, c1)

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank='B', suit='clubs')
            
    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank='A', suit='clubsoda')
            

class TestHand(unittest.TestCase):
    
    def test_simple(self):
        hand = Hand([Card(rank='5', suit='spades')])
        self.assertEqual(hand.score(), 5)
        
    def test_soft_17(self):
        hand = Hand([
            Card(rank='A', suit='spades'),
            Card(rank='6', suit='spades'),
        ])
        self.assertEqual(hand.score(), 17)
            
    def test_hard_17(self):
        hand = Hand([
            Card(rank='A', suit='spades'),
            Card(rank='K', suit='spades'),
            Card(rank='6', suit='spades'),
        ])
        self.assertEqual(hand.score(), 17)
        
    def test_really_hard_14(self):
        hand = Hand([
            Card(rank='A', suit='spades'),
            Card(rank='A', suit='clubs'),
            Card(rank='A', suit='hearts'),
            Card(rank='A', suit='diamonds'),
            Card(rank='K', suit='spades')
        ])
        self.assertEqual(hand.score(), 14)
        
