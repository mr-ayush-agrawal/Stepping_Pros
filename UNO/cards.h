#pragma

#include <iostream>
#include <string.h>
#include <vector>
using namespace std;


class cards
{
    string color; // This is the suite of the card
    char face;    // The Value of the card is teh face of the card
    
public:
    cards(string clr, char num)
    {
        this->color = clr;
        this->face = num;
    }
    void show();
};

vector<cards> CreateDeck();
void suffleDeck(vector<cards> &deck) ;