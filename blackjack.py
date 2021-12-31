from dataclasses import dataclass
from typing import Dict, List, Optional
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
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand: Hand = Hand()
        self.chips: Chips = Chips()

    def receive_card(self, card: Card) -> bool:
        print(f"Player {self.name} has received the card suit and rank: {values[card.rank]} of {card.suit}.")
        return self.hand.add_card(card)

    def make_bet(self):
        pass

    def get_name(self) -> str:
        return self.name

    def get_chips_total(self) -> int:
        return self.chips.total


class Table:
    def __init__(self, players: List[Player] = []):
        self.players: List[Player] = players
        self.deck: Deck = Deck()
        self.playing_status: Dict[Player, bool] = {player: True for player in players}
        self.game_winner: Optional[Player] = None
        pass

    def take_bet(self, player: Player) -> bool:
        while True:
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

    def end_game(self, winner: Optional[Player]):
        if not winner:
            print("\nThe table has won. Sorry you all failed!\n")
        else:
            print(f"Blackjack! Game has been won by player: {winner.get_name()}")

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
                    return True
                else:
                    print("Thank you for playing!")
                    return False

    def update_chips(self, winning_player: Optional[Player]):
        for player in self.players:
            if winning_player == player:
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
                        player_response = int(
                            input(
                                f"\nPlayer: {player.name} - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): "
                            )
                        )
                    except ValueError:
                        print("Invalid. Respond with number 1 or 2.")
                    else:
                        if player_response == 1:
                            self.hit(player)

                            player_hand_value = player.hand.get_hand_sum()
                            print(f"Current hand value is: {player_hand_value}")

                            if player_hand_value == 21:
                                self.game_winner = player
                                self.end_game(winner=self.game_winner)
                                print(f"You have won!")
                                game_ended = True
                            elif player_hand_value > 21:
                                print(f"You have gone bust!")
                                game_ended = True
                        else:
                            self.playing_status[player] = False

                        break

            if not any([self.playing_status[player] for player in self.playing_status]):
                break

        print("Game has ended!")
        self.end_game(winner=self.game_winner)
        self.update_chips(self.game_winner)

        is_continue = self.ask_to_continue_game()
        if not is_continue:
            return
        else:
            return self.run_game()


if __name__ == "__main__":
    player_1 = Player("Jack")
    player_2 = Player("Enemy")
    game_table = Table([player_1, player_2])

    game_table.run_game()
