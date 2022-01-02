from dataclasses import dataclass
from typing import Dict, List, Optional
import random
from abc import ABC, abstractmethod
import random


@dataclass
class CardType:
    num: int
    suit: str or None


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


suits = ("Heart", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.hand: Hand = Hand()
        self.chips: Chips = Chips()

    def receive_card(self, card: Card) -> bool:
        return self.hand.add_card(card)

    def get_name(self) -> str:
        return self.name

    def get_chips_total(self) -> int:
        return self.chips.total


class NormalPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def receive_card(self, card: Card) -> bool:
        print(f"Player {self.name} has received the card suit and rank: {values[card.rank]} of {card.suit}.")
        return super().receive_card(card)


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
        self.chips: Chips = Chips(10000)

    def receive_card(self, card: Card) -> bool:
        print(f"The Dealer has drawn the card suit and rank: {values[card.rank]} of {card.suit}")
        return super().receive_card(card)

    def get_chips_total(self) -> int:
        self.chips: Chips = Chips(10000)
        return self.chips.total  # Dealer has constantly refueled chip amount.


class Deck:
    def __init__(self):
        self.deck: List[Card] = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def __str__(self):
        deck_comp: str = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards: List[Card] = []
        self.value: int = 0
        self.aces: int = 0

    def add_card(self, card: Card) -> bool:
        self.cards.append(card)
        self.value += values[card.rank]
        self.adjust_for_ace()

        return False if self.is_bust() else True

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def get_hand_sum(self) -> int:
        hand_sum = 0
        for card in self.cards:
            hand_sum += values[card.rank]
        return hand_sum

    def is_bust(self) -> bool:
        hand_sum = self.get_hand_sum()
        return True if hand_sum > 21 else False

    def is_blackjack(self) -> bool:
        hand_sum = self.get_hand_sum()
        return True if hand_sum == 21 else False


class Chips:
    def __init__(self, total: int = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0


class Table:
    def __init__(self, players: List[Player]):
        self.players: List[Player] = players
        self.deck: Deck = Deck()
        self.playing_status: Dict[Player, bool] = {player: True for player in players}
        self.game_winner: List[Optional[Player]] = []

    def take_bet(self, player: Player) -> bool:
        while True:
            if isinstance(player, Dealer):
                return True

            try:
                player.chips.bet = int(
                    input(f"\nPlayer: {player.get_name()} - How many chips would you like to bet? ")
                )
            except ValueError:
                print("Invalid. Must bet an integer.")
            else:
                if player.chips.total == 0:
                    print("You have no chips to bet")
                    return False
                elif player.chips.bet > player.chips.total:
                    print(
                        f"Bet exceeds chips amount. Your total chip amount is {player.chips.total}. Input a valid amount."
                    )
                else:
                    break
        return True

    def hit(self, player: Player):
        next_card = self.deck.deal()
        is_card_added = player.receive_card(next_card)
        if not is_card_added:
            # player is bust
            self.playing_status[player] = False
            print(f"Your hand has passed 21 with the value {player.hand.get_hand_sum()}. You are bust.")

    def end_game(self, winner: List[Optional[Player]]):
        if not winner:
            print("No one has won. Sorry you all failed! (P.S. The house always wins though.)\n")
        else:
            print(f"Blackjack! Game has been won by player(s): {', '.join([w.get_name() for w in winner if w])}")

    def display_all_chips(self):
        print("Total chip scores:\n")
        for player in self.players:
            print(f"{player.get_name()}: {player.get_chips_total()}")

    def ask_to_continue_game(self) -> bool:
        self.display_all_chips()

        print()
        while True:
            try:
                is_play = int(input("\nWould you like to continue playing? (1 -> Yes, 2 -> No)"))
            except ValueError:
                print("Invalid. Respond with number 1 or 2.")
            else:
                if is_play == 1:
                    for player in self.playing_status:
                        self.playing_status[player] = True

                    self.game_winner = []
                    return True
                else:
                    print("Thank you for playing!")
                    return False

    def update_chips(self, winning_player: List[Optional[Player]]):
        for player in self.players:
            if player in winning_player:
                player.chips.win_bet()
            else:
                player.chips.lose_bet()

    def run_game(self):
        game_ended = False

        for player in self.players:
            player_chips_bet = self.take_bet(player)
            if not player_chips_bet:
                self.playing_status[player] = False
                continue

        while not game_ended:
            for player in self.players:
                if not self.playing_status[player]:
                    continue

                while True:

                    try:
                        if not isinstance(player, Dealer):
                            player_response = int(
                                input(
                                    f"\nPlayer: {player.name} - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): "
                                )
                            )
                        else:
                            player_response = 1 if player.hand.get_hand_sum() < 18 else 2
                            print(f'\nThe Dealer has chosen to {"HIT" if player_response == 1 else "STAND"}')
                    except ValueError:
                        print("Invalid. Respond with number 1 or 2.")
                    else:
                        if player_response == 1:
                            self.hit(player)

                            player_hand_value = player.hand.get_hand_sum()
                            print(f"Current hand value is: {player_hand_value}")

                            if player_hand_value == 21:
                                self.game_winner.append(player)
                                self.end_game(winner=self.game_winner)
                                if isinstance(player, Dealer):
                                    print(f"The Dealer has won. Everyone else loses.")
                                else:
                                    print(f"Player {player.get_name()} has won!")
                                game_ended = True
                            elif player_hand_value > 21:
                                if isinstance(player, Dealer):
                                    print(f"The Dealer has gone bust!!!")
                                    game_ended = True
                                    for player in self.playing_status:
                                        if self.playing_status[player]:
                                            self.game_winner.append(player)

                        else:
                            print(f"\n{player.name} is standing with hand value at: {player.hand.get_hand_sum()}")
                            self.playing_status[player] = False

                        break

            if not game_ended and not any([self.playing_status[player] for player in self.playing_status]):
                game_ended = True

                # find if any hand is not bust
                hand_sums = []
                for player in self.playing_status:
                    if player.hand.get_hand_sum() <= 21:
                        hand_sums.append((player, player.hand.get_hand_sum()))

                # best hand amongst standing players belongs to
                hand_sums.sort(key=lambda x: x[1])
                self.game_winner.append(hand_sums[-1][0])

        print("Game has ended!")
        self.end_game(winner=self.game_winner)
        self.update_chips(self.game_winner)

        is_continue = self.ask_to_continue_game()
        if not is_continue:
            return
        else:
            return self.run_game()


if __name__ == "__main__":
    player1 = NormalPlayer("Jack")
    player2 = NormalPlayer("Enemy")
    dealer = Dealer()
    game_table = Table(players=[player1, player2, dealer])

    game_table.run_game()
