// #include "cards.cpp"
#include "cards.h"
#include "player.h"
#include <time.h>
#include "Info.cpp"

using namespace std;

vector<cards> CreateDeck();
void suffleDeck(vector<cards> &deck);

void TestMove()
{
    vector<cards> D = CreateDeck();
    suffleDeck(D);
    srand(time(0));
    player P;
    for (int i = 0; i < 7; i++)
    {
        int R = rand() % D.size();
        cards RanCar = D.at(R);
        D.erase(D.begin() + R);
        P.draw(RanCar);
    }
    P.showHand();

    cards Top = D.back();
    D.pop_back();

    cout << "\n\nTop Card is ";
    Top.show();

    P.move(Top, 5);
    P.showHand();
    cout << "\n\nTop Card is ";
    Top.show();
}

int main()
{

    // int NumberOfPlayer = starting_Game();
    // player p[NumberOfPlayer];
    vector<cards> Deck = CreateDeck();
    // suffleDeck(Deck);

    // for(int i=0; i<Deck.size();i++)
    // {
    //     p[i%NumberOfPlayer].draw(Deck[i]);
    // }
    // for(int i=0; i<NumberOfPlayer;i++)
    // {
    //     cout<<"\nCards with player "<<i<<" are";
    //     p[i].showHand();
    // }

    for (cards c : Deck)
        c.show();

    // TestMove();
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
            if (nums[i] == 'W' || nums[i] == 'F')
            {
                cards c("Black", nums[i]);
                deck.push_back(c);
            }
            else
            {
                cards c(clrs[j], nums[i]);
                deck.push_back(c);
            }
        }
    }
    return deck;
}

void suffleDeck(vector<cards> &deck)
{
    srand(time(0));
    for (int i = 0, sz = deck.size(); i < sz; i++)
    {
        swap(deck[i], deck[rand() % sz]);
    }
}
