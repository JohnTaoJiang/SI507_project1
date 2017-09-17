### Intro ###
This project is about testing the given code of Card Game Simulator which has 3 bugs.
The goal is to write testcases with Unittest Module to find out the bugs.

### Structure ###
* **CardTests**
 * test_init: test the constructor of Card class
 * test_toString: test the string method of Card

* **DeckTests**
 * test_init: test the constructor of Deck class
 * test_toString: test the string method of Deck
 * test_popLastCard: test the _pop_card()_ method under default condition(i.e. without input)
 * test_popOneCard: test the _pop_card()_ method with specified input(i.e. pop a specified card from a Deck)
 * test_popAll: test the _pop_card()_ method to check if a deck can be completely pop
 * test_shuffle: test the _shuffle()_ method to check if a deck is shuffled
 * test_replaceAdd: test the _replace_card()_ method with an input Card not in current Deck(i.e. needs to add that Card)
 * test_replaceNotAdd: test the _replace_card()_ method with an input Card already in current Deck(i.e. nothing changes in Deck)
 * test_sortCards: test the sort_cards method to check if a deck can be sorted based on rank and suit at anytime
 * test_deal_hand: test the deal_hand method to see if hand can be dealt up to the full size of current Deck

* **PlayTest**
 * test_func: test the _play_war_game()_ function to check if the return value matches the expected type

* **ShowSongTest**
 * test_func: test the _show_song()_ function to see if the return value matches the expected type and if arbitrary search terms can be used

### Getting Started ###
See requirements.txt
