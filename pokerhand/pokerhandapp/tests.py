#
# @author: Brian
#

from django.test import TestCase
import random
from pokerhandapp.models import pokerCards, categories, Poker, PokerHand


def randomCards():
    rand1 = random.randint(0,51)
    rand2 = random.randint(0,51)
    rand3 = random.randint(0,51)
    rand4 = random.randint(0,51)
    rand5 = random.randint(0,51)
    #print('rand5: %s'%(rand5))
    cards = pokerCards()
    hand1 = cards[rand1]
    hand2 = cards[rand2]
    hand3 = cards[rand3]
    hand4 = cards[rand4]
    hand5 = cards[rand5]
    cardsX = [hand1, hand2, hand3, hand4, hand5]
    return cardsX

cardsX = randomCards()
hand = PokerHand(cardsX)
results = hand.evaluate()
print('randomCards: %s, \n results: %s'%(cardsX, results))

class TestPoker(TestCase):
    """Test for Poker ."""
    def setUP(self):
        #
        pass

    def tearDown(self):
        #
        pass

    def test_onePairX(self):
        cards = ['2 of Clubs', '5 of Diamonds', '2 of Hearts', '7 of Spades', '4 of Diamonds']
        hand = PokerHand(cards)
        results = hand.evaluate()
        self.assertEqual(results, categories('onePair'))

    def test_twoPairsX(self):
        cards = ['7 of Clubs', '5 of Diamonds', '6 of Hearts', '6 of Spades', '7 of Diamonds']
        hand = PokerHand(cards)
        results = hand.evaluate()
        self.assertEqual(results, categories('twoPairs'))

    def test_threeOfaKindX(self):
        cards = ['9 of Clubs', '5 of Diamonds', '9 of Hearts', '7 of Spades', '9 of Diamonds']
        hand = PokerHand(cards)
        results = hand.evaluate()
        self.assertEqual(results, categories('threeOfaKind'))

    def test_fourOfaKindX(self):
        cards = ['6 of Clubs', '5 of Diamonds', '6 of Hearts', '6 of Spades', '6 of Diamonds']
        hand = PokerHand(cards)
        results = hand.evaluate()
        self.assertEqual(results, categories('fourOfaKind'))

    def test_straightX(self):
        cards = ['6 of Clubs', '5 of Diamonds', '3 of Hearts', '4 of Spades', '7 of Diamonds']
        hand = PokerHand(cards)
        results = hand.evaluate()
        self.assertEqual(results, categories('straight'))

    def test_flushX(self):
        cards = ['6 of Clubs', '5 of Clubs', '8 of Clubs', '10 of Clubs', '3 of Clubs']
        hand = PokerHand(cards)
        results = hand.evaluate()
        self.assertEqual(results, categories('flush'))

    def test_straightFlushX(self):
        cards = ['6 of Diamonds', '5 of Diamonds', '7 of Diamonds', '4 of Diamonds', '8 of Diamonds']
        hand = PokerHand(cards)
        results = hand.evaluate()
        self.assertEqual(results, categories('straightFlush'))

class TestPokerHand(TestCase):
    """Test for PokerHand ."""
    def setUP(self):
        #
        pass

    def test_evaluate(self):
        #
        pass

    def checkCards(self):
        #
        pass
