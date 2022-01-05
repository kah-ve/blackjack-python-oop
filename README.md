**Python Blackjack game utilizing OOP, typing, ABC (abstract classes), and a completely contrived factory design pattern!**
This project very basically started from an article I was reading and then I completely took it in another direction to serve the purpose of being a useful tool to practically implement and practice some different types of programming for improvement sake. Also was quite fun.
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
**An example game run (not particularly easy on the eyes or insightful tbh):**

Player Intros:<br>
Thanks for me naming me! - NP <br>
I am the Dealer welcome to the table.<br>
Interesting is what interesting does! - IDP       <br>
I play and I don't play and yet I never stop. - CP<br>
Is it actually a loss if you never actually win? - PLP<br>
<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 1<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 2323<br>
Bet exceeds chips amount. Your total chip amount is 100. Input a valid amount.<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 232<br>
Bet exceeds chips amount. Your total chip amount is 100. Input a valid amount.<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 23<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 223<br>
Bet exceeds chips amount. Your total chip amount is 100. Input a valid amount.<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 23<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 23<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 6 of Clubs.<br>
Current hand value is: 6<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 10 of Diamonds<br>
Current hand value is: 10<br>
Player InterestingDecisionPlayer has received the card suit and rank: 10 of Diamonds.<br>
Current hand value is: 10<br>
<br>
ConservativePlayer is standing with hand value at: 0<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 7 of Heart.<br>
Current hand value is: 7<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 10 of Heart.<br>
Current hand value is: 16<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 2 of Clubs<br>
Current hand value is: 12<br>
<br>
InterestingDecisionPlayer is standing with hand value at: 10<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 10 of Heart.<br>
Current hand value is: 17<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 9 of Clubs.<br>
Your hand has passed 21 with the value 25. You are bust.<br>
Current hand value is: 25<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 2 of Spades<br>
Current hand value is: 14<br>
<br>
PerenniallyLosingPlayer is standing with hand value at: 17<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 4 of Diamonds<br>
Current hand value is: 18<br>
<br>
The Dealer has chosen to STAND<br>
<br>
Dealer is standing with hand value at: 18<br>
Game has ended!<br>
Blackjack! Game has been won by player(s): Dealer<br>
Would the player(s) like to make any comments on their win?<br>
Total chip scores:<br>
<br>
MainCharacterJack: 99<br>
Dealer: 10000<br>
InterestingDecisionPlayer: 77<br>
ConservativePlayer: 77<br>
PerenniallyLosingPlayer: 77<br>
<br>
<br>
Would you like to continue playing? (1 -> Yes, 2 -> No)1<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 1<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 1<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 1<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 1<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 9 of Diamonds.<br>
Current hand value is: 9<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 7 of Diamonds<br>
Current hand value is: 7<br>
Player InterestingDecisionPlayer has received the card suit and rank: 4 of Clubs.<br>
Current hand value is: 4<br>
<br>
ConservativePlayer is standing with hand value at: 0<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 3 of Clubs.<br>
Current hand value is: 3<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 8 of Heart.<br>
Current hand value is: 17<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 7 of Spades<br>
Current hand value is: 14<br>
<br>
InterestingDecisionPlayer is standing with hand value at: 4<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 8 of Spades.<br>
Current hand value is: 11<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 10 of Clubs.<br>
Your hand has passed 21 with the value 27. You are bust.<br>
Current hand value is: 27<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 10 of Spades<br>
Your hand has passed 21 with the value 24. You are bust.<br>
Current hand value is: 24<br>
The Dealer has gone bust!!!<br>
<br>
PerenniallyLosingPlayer is standing with hand value at: 11<br>
Game has ended!<br>
Blackjack! Game has been won by player(s): InterestingDecisionPlayer, ConservativePlayer, PerenniallyLosingPlayer<br>
Would the player(s) like to make any comments on their win?<br>
Total chip scores:<br>
<br>
MainCharacterJack: 98<br>
Dealer: 10000<br>
InterestingDecisionPlayer: 78<br>
ConservativePlayer: 78<br>
PerenniallyLosingPlayer: 78<br>
<br>
<br>
Would you like to continue playing? (1 -> Yes, 2 -> No)1<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 1<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 1<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 1<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 1<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 10 of Diamonds.<br>
Current hand value is: 10<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 7 of Clubs<br>
Current hand value is: 7<br>
Player InterestingDecisionPlayer has received the card suit and rank: 4 of Heart.<br>
Current hand value is: 4<br>
<br>
ConservativePlayer is standing with hand value at: 0<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 11 of Clubs.<br>
Current hand value is: 11<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 6 of Heart.<br>
Current hand value is: 16<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 10 of Clubs<br>
Current hand value is: 17<br>
<br>
InterestingDecisionPlayer is standing with hand value at: 4<br>
<br>
PerenniallyLosingPlayer is standing with hand value at: 11<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 8 of Clubs.<br>
Your hand has passed 21 with the value 24. You are bust.<br>
Current hand value is: 24<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 10 of Diamonds<br>
Your hand has passed 21 with the value 27. You are bust.<br>
Current hand value is: 27<br>
The Dealer has gone bust!!!<br>
Game has ended!<br>
Blackjack! Game has been won by player(s): InterestingDecisionPlayer, ConservativePlayer, PerenniallyLosingPlayer<br>
Would the player(s) like to make any comments on their win?<br>
Total chip scores:<br>
<br>
MainCharacterJack: 97<br>
Dealer: 10000<br>
InterestingDecisionPlayer: 79<br>
ConservativePlayer: 79<br>
PerenniallyLosingPlayer: 79<br>
<br>
<br>
Would you like to continue playing? (1 -> Yes, 2 -> No)1<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 1<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 1<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 1<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 1<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 3 of Heart.<br>
Current hand value is: 3<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 9 of Heart<br>
Current hand value is: 9<br>
Player InterestingDecisionPlayer has received the card suit and rank: 3 of Spades.<br>
Current hand value is: 3<br>
<br>
ConservativePlayer is standing with hand value at: 0<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 2 of Diamonds.<br>
Current hand value is: 2<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 4 of Spades.<br>
Current hand value is: 7<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 10 of Heart<br>
Current hand value is: 19<br>
<br>
InterestingDecisionPlayer is standing with hand value at: 3<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 10 of Clubs.<br>
Current hand value is: 12<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 10 of Clubs.<br>
Current hand value is: 17<br>
<br>
The Dealer has chosen to STAND<br>
<br>
Dealer is standing with hand value at: 19<br>
<br>
PerenniallyLosingPlayer is standing with hand value at: 12<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 6 of Spades.<br>
Your hand has passed 21 with the value 23. You are bust.<br>
Current hand value is: 23<br>
Game has ended!<br>
Blackjack! Game has been won by player(s): Dealer<br>
Would the player(s) like to make any comments on their win?<br>
Total chip scores:<br>
<br>
MainCharacterJack: 96<br>
Dealer: 10000<br>
InterestingDecisionPlayer: 78<br>
ConservativePlayer: 78<br>
PerenniallyLosingPlayer: 78<br>
<br>
<br>
Would you like to continue playing? (1 -> Yes, 2 -> No)2<br>
Thank you for playing!<br>
