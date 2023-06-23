#pragma once

#include "cards.h"
#include <vector>

class player
{
    // string name;
    vector<cards> inHand;

    public :
    void draw(cards newCard); // To add the cards in hand if drawn
    void move(cards Top_Cards); // To remove the card in hand as moved
    void showHand(); //Printing all the cards a player is carrying with Index
};