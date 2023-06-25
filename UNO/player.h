#pragma once

#include "cards.h"
#include <vector>

class player
{
    // string name;
    vector<cards> inHand;
    string Name;
    public :
    void draw(cards newCard); // To add the cards in hand if drawn
    void move(cards &Top_Cards,int); // To remove the card in hand as moved
    void showHand(); //Printing all the cards a player is carrying with Index
    void getName(string); // To get the name of the player 
    string PlayerName(); // To return the Player's Name
};

// Declearing the functions here but to be defined in other file

void player :: draw(cards NewCard)
{
    inHand.emplace_back(NewCard);
}

void player :: showHand()
{
    cout<<endl;

    for (int i =0, n=inHand.size();i<n;i++)
    {
        inHand[i].show();
        cout<<"\t"<<i;
    }
}

void player :: move(cards &Top,int idx)
{
    Top=inHand[idx];
    inHand.erase(inHand.begin() + idx);
}


void player :: getName(string Name)
{
    this->Name = Name;
}

string player :: PlayerName()
{
    return Name;
}