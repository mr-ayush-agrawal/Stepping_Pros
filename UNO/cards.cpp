// This will be converted to the header file later Untill test its a cpp file

# include <iostream>
using namespace std;

class cards 
{
    string color;  // This is the suite of the card
    char face;  // The Value of the card is teh face of the card

    public :
    cards(string clr,char num)
    {
        this->color=clr;
        this->face=num;
    }

    void show()
    {
        // This Function is temporary
        cout<<"\n"<<color<<" -> "<<face;
    }
};
/*
THE CARDS NUMBERS WILL BE AS FOLLOWS :
0-9 -> Will be same as 0-9 respectively
S -> For the Skip
R-> For the Reverse
W -> Wild
T -> Draw 2 (+2)
F -> Draw 4 (+4)
*/

void CreateDeck()
{
    // Creating all the cards present in the Deck
    string clrs[] ={"Blue", "Green","Red", "Yellow"};
    char nums[]={'1','2','3','4','5','6','7','8','9','10','T','S','R','W','F'};
    int numsize=sizeof(nums),clrsize=4;
    for(int i=0;i<numsize;i++)
    {
        for(int j=0;j<clrsize;j++)
        {
            // Creating thje card and Pusding it in a Vector
        }
    }
}