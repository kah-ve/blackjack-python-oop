**Python Blackjack game utilizing OOP, typing, ABC (abstract classes), and a completely contrived factory design pattern!**
This project very basically started from an article I was reading and then I completely took it in another direction to serve the purpose of being a useful tool to practically implement and practice some different types of programming for improvement sake. Also was quite fun.
<br></br>
<br></br>
<br></br>
<br></br>
<br></br>
**An example game run (not particularly easy on the eyes or insightful tbh):**

I am the Dealer welcome to the table.<br>
Interesting is what interesting does! - IDP<br>
I play and I don't play and yet I never stop. - CP    <br>
Is it actually a loss if you never actually win? - PLP<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 25<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 25<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 25<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 25<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 6 of Heart.<br>
Current hand value is: 6<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 8 of Clubs<br>
Current hand value is: 8<br>
Player InterestingDecisionPlayer has received the card suit and rank: 10 of Heart.<br>
Current hand value is: 10<br>
<br>
ConservativePlayer is standing with hand value at: 0<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 2 of Clubs.<br>
Current hand value is: 2<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 9 of Heart.<br>
Current hand value is: 15<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 10 of Diamonds<br>
Current hand value is: 18<br>
<br>
InterestingDecisionPlayer is standing with hand value at: 10<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 10 of Clubs.<br>
Current hand value is: 12<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 5 of Heart.<br>
Current hand value is: 20<br>
<br>
The Dealer has chosen to STAND<br>
<br>
Dealer is standing with hand value at: 18<br>
<br>
PerenniallyLosingPlayer is standing with hand value at: 12<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 4 of Spades.<br>
Your hand has passed 21 with the value 24. You are bust.<br>
Current hand value is: 24<br>
Game has ended!<br>
Blackjack! Game has been won by player(s): Dealer<br>
Would the player(s) like to make any comments on their win?<br>
Total chip scores:<br>
<br>
MainCharacterJack: 75<br>
Dealer: 10000<br>
InterestingDecisionPlayer: 75<br>
ConservativePlayer: 75<br>
PerenniallyLosingPlayer: 75<br>
<br>
<br>
Would you like to continue playing? (1 -> Yes, 2 -> No)1<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 22<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 55<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 7353<br>
Bet exceeds chips amount. Your total chip amount is 75. Input a valid amount.<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 53<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 1123<br>
Bet exceeds chips amount. Your total chip amount is 75. Input a valid amount.<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 11   <br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 2<br>
<br>
MainCharacterJack is standing with hand value at: 0<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 8 of Spades<br>
Current hand value is: 8<br>
Player InterestingDecisionPlayer has received the card suit and rank: 4 of Heart.<br>
Current hand value is: 4<br>
<br>
ConservativePlayer is standing with hand value at: 0<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 11 of Spades.<br>
Current hand value is: 11<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 4 of Clubs<br>
Current hand value is: 12<br>
<br>
InterestingDecisionPlayer is standing with hand value at: 4<br>
<br>
PerenniallyLosingPlayer is standing with hand value at: 11<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 11 of Diamonds<br>
Your hand has passed 21 with the value 23. You are bust.<br>
Current hand value is: 23<br>
The Dealer has gone bust!!!<br>
Game has ended!<br>
Blackjack! Game has been won by player(s): MainCharacterJack, InterestingDecisionPlayer, ConservativePlayer, PerenniallyLosingPlayer<br>
Would the player(s) like to make any comments on their win?<br>
Total chip scores:<br>
<br>
MainCharacterJack: 97<br>
Dealer: 10000<br>
InterestingDecisionPlayer: 130<br>
ConservativePlayer: 128<br>
PerenniallyLosingPlayer: 86<br>
<br>
<br>
Would you like to continue playing? (1 -> Yes, 2 -> No)1<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 1224<br>
Bet exceeds chips amount. Your total chip amount is 97. Input a valid amount.<br>
<br>
Player: MainCharacterJack - How many chips would you like to bet? 11<br>
<br>
Player: InterestingDecisionPlayer - How many chips would you like to bet? 52<br>
<br>
Player: ConservativePlayer - How many chips would you like to bet? 66<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 523<br>
Bet exceeds chips amount. Your total chip amount is 86. Input a valid amount.<br>
<br>
Player: PerenniallyLosingPlayer - How many chips would you like to bet? 34<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 3 of Clubs.<br>
Current hand value is: 3<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 10 of Spades<br>
Current hand value is: 10<br>
Player InterestingDecisionPlayer has received the card suit and rank: 10 of Spades.<br>
Current hand value is: 10<br>
<br>
ConservativePlayer is standing with hand value at: 0<br>
Player PerenniallyLosingPlayer has received the card suit and rank: 11 of Clubs.<br>
Current hand value is: 11<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 6 of Spades.<br>
Current hand value is: 9<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 6 of Diamonds<br>
Current hand value is: 16<br>
<br>
InterestingDecisionPlayer is standing with hand value at: 10<br>
<br>
PerenniallyLosingPlayer is standing with hand value at: 11<br>
<br>
Player: MainCharacterJack - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): 1<br>
Player MainCharacterJack has received the card suit and rank: 10 of Clubs.<br>
Current hand value is: 19<br>
<br>
The Dealer has chosen to HIT<br>
The Dealer has drawn the card suit and rank: 9 of Clubs<br>
Your hand has passed 21 with the value 25. You are bust.<br>
Current hand value is: 25<br>
The Dealer has gone bust!!!<br>
Game has ended!<br>
Blackjack! Game has been won by player(s): MainCharacterJack, InterestingDecisionPlayer, ConservativePlayer, PerenniallyLosingPlayer<br>
Would the player(s) like to make any comments on their win?<br>
Total chip scores:<br>
<br>
MainCharacterJack: 108<br>
Dealer: 10000<br>
InterestingDecisionPlayer: 182<br>
ConservativePlayer: 194<br>
PerenniallyLosingPlayer: 120<br>
<br>
<br>
Would you like to continue playing? (1 -> Yes, 2 -> No)2<br>
Thank you for playing!<br>
