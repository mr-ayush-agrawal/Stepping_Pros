// #include "cards.cpp"
#include "cards.h"
#include "player.h"

using namespace std;

int main()
{
    player p;
    // cards c1("wrteew",'d');
    // cards c2("feew",'g');
    // cards c3("wrew",'a');
    // cards c4("dsgfasd",'f');

    // p.draw(c1);
    // p.draw(c2);
    // p.draw(c3);
    // p.draw(c4);

    // p.showHand();

    vector<cards> deck = CreateDeck();
    for (cards c : deck)
        c.show();
}