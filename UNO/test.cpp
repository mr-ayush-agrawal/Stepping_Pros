// #include "cards.cpp"
#include "cards.h"
#include "player.h"
#include "GameFiles.h"

using namespace std;

vector<cards> CreateDeck();
void suffleDeck(vector<cards> &deck) ;


int main()
{
    // player p;
    cards c1("wrteew",'d');
    cards c2("feew",'g');
    cards c3("wrew",'a');
    cards c4("dsgfasd",'f');

    c1.show();

    // p.draw(c1);
    // p.draw(c2);
    // p.draw(c3);
    // p.draw(c4);

    // p.showHand();

    vector<cards> deck = CreateDeck();
    for (cards c : deck)
        c.show();

    cout<<"asdfhsadhfkasdhfsdhfisduhf";
    
    suffleDeck(deck);
        for (cards c : deck)
        c.show();

    return 0;
}










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
