# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in
# the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail.
# If more than 3 tests fail, it should be because multiple of
# the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like,
# but you should try to make these tests well-organized
# and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########


class CardTests(unittest.TestCase):
    def setUp(self):
        self.Card1 = Card(1, 5)
        self.Card2 = Card(2, 13)

    def test_init(self):
        self.assertEqual(self.Card1.rank, 5)
        self.assertEqual(self.Card1.rank_num, 5)
        self.assertEqual(self.Card1.suit, "Clubs")
        self.assertEqual(self.Card2.rank, "King")
        self.assertEqual(self.Card2.rank_num, 13)
        self.assertEqual(self.Card2.suit, "Hearts")

    def test_toString(self):
        self.assertEqual(str(self.Card1), "5 of Clubs")
        self.assertEqual(str(self.Card2), "King of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck1 = Deck()

    def test_init(self):
        self.assertTrue(isinstance(self.deck1.cards, list))
        self.assertTrue(len(self.deck1.cards) == 52)
        for c in self.deck1.cards:
            self.assertTrue(
                isinstance(c, Card),
                "testing if every element of cards is a Card object")

    def test_toString(self):
        cardsStr = str(self.deck1)
        self.assertTrue(isinstance(cardsStr, str))
        cardsLs = cardsStr.split('\n')
        self.assertTrue(len(cardsLs) == 52)

    def test_popLastCard(self):
        lastCard = self.deck1.cards[-1]
        cardsPopLast = self.deck1.pop_card()
        self.assertEqual(
            isinstance(cardsPopLast, Card),
            isinstance(lastCard, Card))
        self.assertEqual(len(self.deck1.cards), 51)
        self.assertEqual(
            str(lastCard), str(cardsPopLast),
            "make sure it is the last card that be popped by default")

    def test_popOneCard(self):
        cardtoPop = self.deck1.cards[48]
        cardsPopOne = self.deck1.pop_card(48)
        self.assertEqual(
            isinstance(cardsPopOne, Card),
            isinstance(cardtoPop, Card))
        self.assertEqual(len(self.deck1.cards), 51)
        self.assertEqual(str(cardtoPop), str(cardsPopOne))

    def test_popAll(self):
        for i in range(0, 52):
            self.deck1.pop_card()
        self.assertTrue(len(self.deck1.cards) == 0)

    def test_shuffle(self):
        orignCards = str(self.deck1)
        self.deck1.shuffle()
        self.assertTrue(str(self.deck1) != orignCards)

    def test_replaceAdd(self):
        cardtoAdd = self.deck1.pop_card(30)
        self.deck1.replace_card(cardtoAdd)
        self.assertTrue(len(self.deck1.cards) == 52)
        self.assertTrue(
            str(self.deck1.cards[-1]) == str(cardtoAdd),
            "testing if the card has been added to the back of deck")

    def test_replaceNotAdd(self):
        cardtoAdd = Card()
        orignCards = str(self.deck1)
        self.deck1.replace_card(cardtoAdd)
        self.assertTrue(str(self.deck1) == orignCards)
        cardtoAdd1 = self.deck1.cards[15]
        cardtoAdd2 = self.deck1.cards[30]
        self.deck1.replace_card(cardtoAdd1)
        self.deck1.replace_card(cardtoAdd2)
        self.assertTrue(str(self.deck1) == orignCards)

    def test_sortCards(self):
        for cnt, i in enumerate(range(51, -1, -10)):
            self.deck1.pop_card(i)   # pop some cards from deck
        self.deck1.shuffle()
        shufDeck = str(self.deck1)
        newDeck = Deck()
        for cnt, i in enumerate(range(51, -1, -10)):
            newDeck.pop_card(i)   # pop the same cards as deck1 from newDeck
        self.deck1.sort_cards()
        self.assertTrue(len(self.deck1.cards) == 52 - cnt - 1)
        self.assertTrue(str(self.deck1) == newDeck)

    def test_deal_hand(self):
        hand = self.deck1.deal_hand(10)
        self.assertTrue(isinstance(hand, list))
        self.assertTrue(len(hand) == 10)
        for card in hand:
            self.assertTrue(isinstance(card, Card))
        curSize = len(self.deck1.cards)
        self.assertTrue(curSize == 52 - 10)
        hand2 = self.deck1.deal_hand(curSize)
        self.assertTrue(
            len(hand2) == curSize,
            "testing if the hand can be dealt up to the size of current deck")


class PlayTest(unittest.TestCase):
    def test_func(self):
        self.assertTrue(isinstance(play_war_game(True), tuple))
        self.assertTrue(isinstance(play_war_game(True)[0], str))
        self.assertTrue(isinstance(play_war_game(True)[1], int))
        self.assertTrue(isinstance(play_war_game(True)[2], int))


class ShowSongTest(unittest.TestCase):
    def test_func(self):
        self.assertTrue(
            isinstance(show_song("loser"), helper_functions.Song),
            "testing if any term can be searched")
        self.assertTrue(isinstance(show_song("love"), helper_functions.Song))

if __name__ == "__main__":
    unittest.main(verbosity=2)
