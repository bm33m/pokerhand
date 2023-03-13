#
# @author: Brian
#

#from django.db import models
# Create your models here.

class Poker():
    """Poker cards ."""
    def __init__(self, arg=52):
        self.numberOfCards = arg
        self.cards = pokerCards()
        selt.categories = categories()

    def onePairX(self, cardP01, cardP02, cardP03, cardP04, cardP05):
        return onePair(cardP01, cardP02, cardP03, cardP04, cardP05)

    def twoPairsX(self, cardP01, cardP02, cardP03, cardP04, cardP05):
        return twoPairs(cardP01, cardP02, cardP03, cardP04, cardP05)

    def threeOfaKindX(self, cardP01, cardP02, cardP03, cardP04, cardP05):
        return threeOfaKind(cardP01, cardP02, cardP03, cardP04, cardP05)

    def fourOfaKindX(self, cardP01, cardP02, cardP03, cardP04, cardP05):
        return fourOfaKind(cardP01, cardP02, cardP03, cardP04, cardP05)

    def straightX(self, cardS01, cardS02, cardS03, cardS04, cardS05):
        return straight(cardS01, cardS02, cardS03, cardS04, cardS05)

    def flushX(self, cardF01, cardF02, cardF03, cardF04, cardF05):
        return flush(cardF01, cardF02, cardF03, cardF04, cardF05)

    def straightFlushX(self, cardF01, cardF02, cardF03, cardF04, cardF05):
        return straightFlush(cardF01, cardF02, cardF03, cardF04, cardF05)

class PokerHand(Poker):
    """Poker hand tool to evaluate cards ."""
    def __init__(self, arg):
        #super(, self).__init__()
        self.cards = arg
        self.hand = 5

    def evaluate(self):
        try:
            cardsX = self.cards
            size = len(cardsX)
            if(size != self.hand):
                return 'Please select %s cards only.'%(self.hand)
            card01 = cardsX[0]
            card02 = cardsX[1]
            card03 = cardsX[2]
            card04 = cardsX[3]
            card05 = cardsX[4]
            validX = self.validCards([card01, card02, card03, card04, card05])
            if(validX == False):
                return 'Please submit %s valid cards only. %s'%(self.hand, pokerCards())
            check01 = self.checkCards(card01, [card02, card03, card04, card05])
            check02 = self.checkCards(card02, [card01, card03, card04, card05])
            check03 = self.checkCards(card03, [card01, card02, card04, card05])
            check04 = self.checkCards(card04, [card01, card02, card03, card05])
            check05 = self.checkCards(card05, [card01, card02, card03, card04])
            totalC = check01 + check02 + check03 + check04 + check05
            if(totalC > 0):
                return 'Please select each card only once. ...totalC: %s'%(totalC)
            cardX01 = card01.split(' ')
            cardX02 = card02.split(' ')
            cardX03 = card03.split(' ')
            cardX04 = card04.split(' ')
            cardX05 = card05.split(' ')
            resultsX = self._results(cardX01, cardX02, cardX03, cardX04, cardX05)
            return resultsX
        except Exception as e:
            print('evaluate: %s'%(e))
        return '...undefined...'

    def validCards(self, cards):
        try:
            cardsX = pokerCards()
            for x in cards:
                xy = x in cardsX
                if(xy == False):
                    return False
            return True
        except Exception as e:
            print('validCards: %s'%(e))
        return False

    def checkCards(self, cardX, cards):
        return checkPairs(cardX, cards)

    def _results(self, cardX01, cardX02, cardX03, cardX04, cardX05):
        straightFlushX = straightFlush(cardX01, cardX02, cardX03, cardX04, cardX05)
        if(straightFlushX):
            return categories('straightFlush')
        fourOfaKindX = fourOfaKind(cardX01, cardX02, cardX03, cardX04, cardX05)
        if(fourOfaKindX):
            return categories('fourOfaKind')
        flushX = flush(cardX01, cardX02, cardX03, cardX04, cardX05)
        if(flushX):
            return categories('flush')
        straightX = straight(cardX01, cardX02, cardX03, cardX04, cardX05)
        if(straightX):
            return categories('straight')
        threeOfaKindX = threeOfaKind(cardX01, cardX02, cardX03, cardX04, cardX05)
        if(threeOfaKindX):
            return categories('threeOfaKind')
        twoPairsX = twoPairs(cardX01, cardX02, cardX03, cardX04, cardX05)
        if(twoPairsX):
            return categories('twoPairs')
        onePairX = onePair(cardX01, cardX02, cardX03, cardX04, cardX05)
        if(onePairX):
            return categories('onePair')
        return categories('highCard')

def categories(rank="all"):
    results = {
        'fiveOfaKind': 'Five of a kind',
        'straightFlush': 'Straight flush',
        'fourOfaKind': 'Four of a kind',
        'fullHouse': 'Full house',
        'flush': 'Flush',
        'straight': 'Straight',
        'threeOfaKind': 'Three of a Kind',
        'twoPairs': 'Two pairs',
        'onePair': 'One pair',
        'highCard': 'High card',
    }
    if(rank == 'all'):
        return results
    return results[rank]

def pokerCards(arg=52):
    cards = [
      'Ace of Clubs',
      '2 of Clubs',
      '3 of Clubs',
      '4 of Clubs',
      '5 of Clubs',
      '6 of Clubs',
      '7 of Clubs',
      '8 of Clubs',
      '9 of Clubs',
      '10 of Clubs',
      'Jack of Clubs',
      'Queen of Clubs',
      'King of Clubs',
      #
      'Ace of Diamonds',
      '2 of Diamonds',
      '3 of Diamonds',
      '4 of Diamonds',
      '5 of Diamonds',
      '6 of Diamonds',
      '7 of Diamonds',
      '8 of Diamonds',
      '9 of Diamonds',
      '10 of Diamonds',
      'Jack of Diamonds',
      'Queen of Diamonds',
      'King of Diamonds',
      ##################
      'Ace of Hearts',
      '2 of Hearts',
      '3 of Hearts',
      '4 of Hearts',
      '5 of Hearts',
      '6 of Hearts',
      '7 of Hearts',
      '8 of Hearts',
      '9 of Hearts',
      '10 of Hearts',
      'Jack of Hearts',
      'Queen of Hearts',
      'King of Hearts',
      #
      'Ace of Spades',
      '2 of Spades',
      '3 of Spades',
      '4 of Spades',
      '5 of Spades',
      '6 of Spades',
      '7 of Spades',
      '8 of Spades',
      '9 of Spades',
      '10 of Spades',
      'Jack of Spades',
      'Queen of Spades',
      'King of Spades',
      #
    ]
    return cards

def onePair(cardP01, cardP02, cardP03, cardP04, cardP05):
    totalP = pairs(cardP01, cardP02, cardP03, cardP04, cardP05)
    #if((totalP > 1)&(totalP < 4)):
    #    print('totalP: %s'%(totalP))
    if(totalP == 2):
       return True
    return False

def twoPairs(cardP01, cardP02, cardP03, cardP04, cardP05):
    totalP = pairs(cardP01, cardP02, cardP03, cardP04, cardP05)
    #if((totalP > 3)&(totalP < 6)):
    #    print('totalP: %s'%(totalP))
    sameX = False
    if(totalP == 4):
        sameX = fourSameCards(cardP01, cardP02, cardP03, cardP04, cardP05, 'twoPairs')
        if(sameX == False):
            return True
    return False

def threeOfaKind(cardP01, cardP02, cardP03, cardP04, cardP05):
    totalK = pairs(cardP01, cardP02, cardP03, cardP04, cardP05)
    if(totalK == 3):
       return True
    return False

def fourOfaKind(cardP01, cardP02, cardP03, cardP04, cardP05):
    totalK = pairs(cardP01, cardP02, cardP03, cardP04, cardP05)
    if(totalK == 4):
       return fourSameCards(cardP01, cardP02, cardP03, cardP04, cardP05, 'fourOfaKind')
    return False

def pairs(cardP01, cardP02, cardP03, cardP04, cardP05):
    pairs2 = [cardP01[0], cardP02[0], cardP03[0], cardP04[0], cardP05[0]]
    hand01 = checkPairs(pairs2[0], [pairs2[1], pairs2[2], pairs2[3], pairs2[4]])
    hand02 = checkPairs(pairs2[1], [pairs2[0], pairs2[2], pairs2[3], pairs2[4]])
    hand03 = checkPairs(pairs2[2], [pairs2[0], pairs2[1], pairs2[3], pairs2[4]])
    hand04 = checkPairs(pairs2[3], [pairs2[0], pairs2[1], pairs2[2], pairs2[4]])
    hand05 = checkPairs(pairs2[4], [pairs2[0], pairs2[1], pairs2[2], pairs2[3]])
    totalPairs = hand01 + hand02 + hand03 + hand04 + hand05
    return totalPairs

def checkPairs(cardX, cards):
    #print('cardX: %s'%(cardX))
    for x in cards:
        if(x == cardX):
            #print('cardX: %s ==  x: %s'%(cardX, x))
            return 1
    return 0

def fourSameCards(cardP01, cardP02, cardP03, cardP04, cardP05, kind='fourOfaKind'):
    sameKind = [cardP01[0], cardP02[0], cardP03[0], cardP04[0], cardP05[0]]
    sameX = 5
    for x in sameKind:
        if x != sameKind[0]:
          sameX = sameX - 1
        if x != sameKind[1]:
          sameX = sameX - 1
        if x != sameKind[2]:
          sameX = sameX - 1
        if x != sameKind[3]:
          sameX = sameX - 1
        if x != sameKind[4]:
          sameX = sameX - 1
    #print('kind: %s, sameX: %s'%(kind, sameX))
    if(sameX == -3):
        return True
    return False

def straight(cardS01, cardS02, cardS03, cardS04, cardS05):
    straightS = [cardS01[0], cardS02[0], cardS03[0], cardS04[0], cardS05[0]]
    #print('1. straightS: %s'%(straightS))
    sortCards(straightS)
    #print('2. straightS: %s'%(straightS))
    straightX = checkStraights(straightS)
    return straightX

def sortCards(cards):
    symbolsToNumbers(cards)
    l = len(cards)
    for x in range(0, l - 1):
        for y in range(x + 1, l):
            if(cards[y] < cards[x]):
                temp = cards[y]
                cards[y] = cards[x]
                cards[x] = temp

def symbolsToNumbers(cards):
    royals = {'Ace': 1, 'Jack': 11, 'Queen': 12, 'King': 13}
    i = 0
    done = False
    for x in cards:
        if(x == 'Ace'):
            cards[i] = royals['Ace']
            done = True
        else:
            if(x == 'Jack'):
                cards[i] = royals['Jack']
                done = True
            else:
                if(x == 'Queen'):
                    cards[i] = royals['Queen']
                    done = True
                else:
                    if(x == 'King'):
                        cards[i] = royals['King']
                        done = True
        if(done == False):
            cards[i] = int(x)
        i = i + 1
        done = False

def checkStraights(cards):
    l = len(cards)
    i = 1
    for x in cards[0:l-1]:
        y = x + 1
        if(y != cards[i]):
            return False
        i = i +1
    return True

def flush(cardF01, cardF02, cardF03, cardF04, cardF05):
    hand = 5
    flushF = [cardF01[2], cardF02[2], cardF03[2], cardF04[2], cardF05[2]]
    hand01 = checkFlush(cardF01[2], flushF)
    hand02 = checkFlush(cardF02[2], flushF)
    hand03 = checkFlush(cardF03[2], flushF)
    hand04 = checkFlush(cardF04[2], flushF)
    hand05 = checkFlush(cardF05[2], flushF)
    totalFlush = hand01 + hand02 + hand03 + hand04 + hand05
    if(totalFlush != hand):
        return False
    return True

def checkFlush(cardF, cards):
    for x in cards:
        if(x != cardF):
            return 0
    return 1

def straightFlush(cardF01, cardF02, cardF03, cardF04, cardF05):
    flushX = flush(cardF01, cardF02, cardF03, cardF04, cardF05)
    if(flushX == False):
        return False
    straightX = straight(cardF01, cardF02, cardF03, cardF04, cardF05)
    return straightX

def fullHouse(cardF01, cardF02, cardF03, cardF04, cardF05):
    pass

def fiveOfaKind(cardP01, cardP02, cardP03, cardP04, cardP05):
    #totalK = pairs(cardP01, cardP02, cardP03, cardP04, cardP05)
    #if(totalK == 5):
    #   return True
    #return False
    pass

def highCard(cardH01, cardH02, cardH03, cardH04, cardH05):
    pass
