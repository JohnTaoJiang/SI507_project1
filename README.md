### Intro ###
This project is about testing the given code of Card Game Simulator which has 3 bugs.
The goal is to write testcases with Unittest Module to find out the bugs.

### Structure ###
* **SI507F17_project1_cards.py:** definition of class Card and Deck
* **SI507F17_project1_tests.py:** testcases for functionality of methods in Card and Deck
    * **CardTests**
      * **_test_init_**: test the constructor of Card class
      * **_test_toString_**: test the string method of Card

    * **DeckTests**
      * **_test_init_**: test the constructor of Deck class
      * **_test_toString_**: test the string method of Deck
      * **_test_popLastCard_**: test the _pop_card()_ method under default condition(i.e. without input)
      * **_test_popOneCard_**: test the _pop_card()_ method with specified input(i.e. pop a specified card from a Deck)
      * **_test_popAll_**: test the _pop_card()_ method to check if a deck can be completely pop
      * **_test_shuffle_**: test the _shuffle()_ method to check if a deck is shuffled
      * **_test_replaceAdd_**: test the _replace_card()_ method with an input Card not in current Deck(i.e. needs to add that Card)
      * **_test_replaceNotAdd_**: test the _replace_card()_ method with an input Card already in current Deck(i.e. nothing changes in Deck)
      * **_test_sortCards_**: test the _sort_cards()_ method to check if a deck can be sorted based on rank and suit at anytime
      * **_test_deal_hand_**: test the _deal_hand()_ method to see if hand can be dealt up to the full size of current Deck

    * **PlayTest**
      * **_test_func_**: test the _play_war_game()_ function to check if the return value matches the expected type

    * **ShowSongTest**
      * **_test_func_**: test the _show_song()_ function to see if the return value matches the expected type and if arbitrary search terms can be used

### Getting Started ###
Please see **_code_description_507F17project1.txt_** & **_requirements.txt_**.
