#include <iostream>
#include <string.h>
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

    void show()
    {
        // This Function is temporary
        cout << "\n"
             << color << "\t-> " << face;
    }
};

 vector<cards> CreateDeck();
/*vector<cards> CreateDeck()
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
}*/


void suffleDeck(vector<cards> &deck);