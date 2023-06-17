// This will be converted to the header file later Untill test its a cpp file
#include <vector>
#include <stdlib.h>
#include <time.h>
#include "cards.h"



/*
THE CARDS NUMBERS WILL BE AS FOLLOWS :
0-9 -> Will be same as 0-9 respectively
S -> For the Skip
R-> For the Reverse
W -> Wild
T -> Draw 2 (+2)
F -> Draw 4 (+4)
*/

vector<cards> CreateDeck()
{
    // Creating all the cards present in the Deck
    string clrs[] = {"Blue", "Green", "Red", "Yellow"};
    char nums[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'T', 'S', 'R', 'W', 'F'};
    int numsize = sizeof(nums), clrsize = 4;
    vector<cards> deck;
    for (int i = 0; i < numsize; i++)
    {
        for (int j = 0; j < clrsize; j++)
        {
            // Creating thje card and Pusding it in a Vector
            cards c(clrs[j], nums[i]);
            deck.push_back(c);
        }
    }
    return deck;
}

void suffleDeck(vector<cards> &deck) 
{
    srand(time(0));
    for (int i=0,sz=deck.size(); i<sz;i++)
    {
        swap(deck[i],deck[rand()%sz]);
    }
}

/*int main()
{
    vector<cards> deck = CreateDeck();
    suffleDeck(deck);
    for (cards c : deck)
        c.show();
    return 0;
}*/