#include "player.h"
#include "info.cpp"
#include "math.h"
void MoveandRotation(player Players[], int NumberOfPlayers, vector<cards> &Deck, cards &TopCard)
{
    int move, rev = 0;
    for (int i = 60; Deck.size() != 0; i = i + pow(-1, rev))
    {
        how_to_play();
    Again:
        cout << "\nIts Move of " << Players[i % NumberOfPlayers].PlayerName() << endl;
        Players[i % NumberOfPlayers].showHand();
        cout << "\nEnter the Index\n";
        cin >> move;
        if (move > Players[i % NumberOfPlayers].CardsCount() || move < -3)
        {
            cout << "Enter a Valid Move\n";
            goto Again;
        }
        else if (move == Players[i % NumberOfPlayers].CardsCount())
        {
            Players[i % NumberOfPlayers].draw(Deck.back());
            Deck.pop_back();
        }
        switch (move)
        {
        case -1:
            rules();
            goto Again;
            break;
        case -2:
            PowerCards();
            goto Again;
            break;
        case -3:
            cout << "\nCards Remaining in Deck are " << Deck.size();
            goto Again;
            break;

        default:
            
            break;
        }
    }
}
