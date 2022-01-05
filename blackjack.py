from dataclasses import dataclass
from typing import Dict, List, Optional, Iterable
import random
from abc import ABC, abstractmethod
import random
from enum import IntEnum, Enum, auto
from collections import Callable
import logging


@dataclass
class CardType:
    num: int
    suit: str or None


class Decision(IntEnum):
    hit = 1
    stand = 2


class PlayerTypes(Enum):
    Normal = auto()
    Dealer = auto()
    Interesting = auto()
    Conservative = auto()
    PerennialLoser = auto()


# Blackjack Card/Deck rules defined
class Card:
    suits: Iterable[str] = ("Heart", "Diamonds", "Spades", "Clubs")

    values: Dict[str, int] = {
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

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


# All Player Types and their inherit skills and overwhelming flaws


class Player(ABC, Callable):  # type: ignore
    def __init__(self):
        self.hand: Hand = Hand()
        self.chips: Chips = Chips()

    @staticmethod
    @abstractmethod
    def get_type() -> PlayerTypes:
        pass

    @classmethod
    @abstractmethod
    def signature_comment(cls) -> str:
        pass

    @abstractmethod
    def response_to_hit_or_stand(self):
        pass

    def get_chips_total(self) -> int:
        return self.chips.total

    def get_name(self):
        return self.name

    def receive_card(self, card: Card) -> bool:
        return self.hand.add_card(card)

    @abstractmethod
    def __call__(self, name: str = ""):
        pass


# Simple and Contrived Factory!
class PlayerFactory:
    registry: Dict[PlayerTypes, Player] = dict()

    @classmethod
    def get_player(cls, player_type: PlayerTypes) -> Player:
        if player_type not in cls.registry:
            raise Exception(
                f"The {player_type} you have selected has not been registered to this factory. Maybe try later?"
            )
        return cls.registry[player_type]

    @classmethod
    def register(cls, player: Player) -> None:
        player_type = player.get_type()
        cls.registry[player_type] = player

    def __call__(self, player_type: PlayerTypes, name: str = None) -> Player:
        if name:
            return self.registry[player_type](name)
        else:
            return self.registry[player_type]()


# Rest of the Player Types
@PlayerFactory.register
class NormalPlayer(Player):
    def __init__(self, name: str):
        super().__init__()
        print("Thanks for me naming me!")
        self.name = name

    def receive_card(self, card: Card) -> bool:
        print(f"Player {self.name} has received the card suit and rank: {Card.values[card.rank]} of {card.suit}.")
        return super().receive_card(card)

    @staticmethod
    def get_type() -> PlayerTypes:
        return PlayerTypes.Normal

    @classmethod
    def signature_comment(cls) -> str:
        return "I am a normal dull player. I neither win or lose consistently."

    def response_to_hit_or_stand(self):
        pass

    def __call__(self, name: str):
        return self.__init__(name)


@PlayerFactory.register
class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Dealer"
        self.chips: Chips = Chips(10000)
        print("I am the Dealer welcome to the table.")

    def receive_card(self, card: Card) -> bool:
        print(f"The Dealer has drawn the card suit and rank: {Card.values[card.rank]} of {card.suit}")
        return super().receive_card(card)

    def get_chips_total(self) -> int:
        self.chips: Chips = Chips(10000)
        return self.chips.total  # Dealer has constantly refueled chip amount.

    @staticmethod
    def get_type() -> PlayerTypes:
        return PlayerTypes.Dealer

    @classmethod
    def signature_comment(cls) -> str:
        return "I am actually not a player, but the host. Not sure why I am gathered with these individuals."

    def response_to_hit_or_stand(self):
        pass

    def __call__(self, name: str):
        return self.__init__()


@PlayerFactory.register
class PerenniallyLosingPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "PerenniallyLosingPlayer"
        print("Is it actually a loss if you never actually win? - PLP")

    def receive_card(self, card: Card) -> bool:
        print(f"Player {self.name} has received the card suit and rank: {Card.values[card.rank]} of {card.suit}.")
        return super().receive_card(card)

    @staticmethod
    def get_type() -> PlayerTypes:
        return PlayerTypes.PerennialLoser

    @classmethod
    def signature_comment(cls) -> str:
        return "Pain! From the ghastly eyrie to the ends of the earth, I cannot remember winning."

    def response_to_hit_or_stand(self):
        if self.hand.get_hand_sum() < 10:
            return Decision.hit
        else:
            return Decision.stand

    def __call__(self, name: str):
        return self.__init__()


@PlayerFactory.register
class InterestingDecisionPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "InterestingDecisionPlayer"
        print("Interesting is what interesting does! - IDP")

    def receive_card(self, card: Card) -> bool:
        print(f"Player {self.name} has received the card suit and rank: {Card.values[card.rank]} of {card.suit}.")
        return super().receive_card(card)

    @staticmethod
    def get_type() -> PlayerTypes:
        return PlayerTypes.Interesting

    @classmethod
    def signature_comment(cls) -> str:
        return "I don't play to win. I play because I can!"

    def response_to_hit_or_stand(self):
        if self.hand.get_hand_sum() < 14 and self.hand.get_hand_sum() > 0:
            return Decision.stand
        else:
            return Decision.hit

    def __call__(self, name: str):
        return self.__init__()


@PlayerFactory.register
class ConservativePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "ConservativePlayer"
        print("I play and I don't play and yet I never stop. - CP")

    def receive_card(self, card: Card) -> bool:
        print(f"Player {self.name} has received the card suit and rank: {Card.values[card.rank]} of {card.suit}.")
        return super().receive_card(card)

    @staticmethod
    def get_type() -> PlayerTypes:
        return PlayerTypes.Conservative

    @classmethod
    def signature_comment(cls) -> str:
        return "One small game a day, never makes a giant leap to bankruptcy my friends! (P.S. Do not ever use money. I am not joking.)"

    def response_to_hit_or_stand(self):
        if self.hand.get_hand_sum() != -42:
            return Decision.stand
        else:
            print("Game has broken! GGs. You are an amazingly astute player.")

    def __call__(self, name: str):
        return self.__init__()


# Deck, Hand, Chips, and Table (the game runner and controller) below
class Deck:
    def __init__(self):
        self.deck: List[Card] = []
        for suit in Card.suits:
            for rank, value in Card.values.items():
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
        self.value += Card.values[card.rank]
        self.adjust_for_ace()

        return False if self.is_bust() else True

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def get_hand_sum(self) -> int:
        hand_sum = 0
        for card in self.cards:
            hand_sum += Card.values[card.rank]
        return hand_sum

    def is_bust(self) -> bool:
        hand_sum = self.get_hand_sum()
        return True if hand_sum > 21 else False

    def is_blackjack(self) -> bool:
        hand_sum = self.get_hand_sum()
        return True if hand_sum == 21 else False

    def reset(self):
        self.cards: List[Card] = []
        self.value: int = 0
        self.aces: int = 0


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
            if player.get_type() == PlayerTypes.Dealer:
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
            print("Would the player(s) like to make any comments on their win?")
            for player in winner:
                player.signature_comment()  # type:ignore

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
                        player.hand.reset()

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
                        if player.get_type() == PlayerTypes.Dealer:
                            player_response = Decision.hit if player.hand.get_hand_sum() < 18 else Decision.stand
                            print(f'\nThe Dealer has chosen to {"HIT" if player_response == 1 else "STAND"}')
                        elif player.get_type() != PlayerTypes.Normal:
                            player_response = player.response_to_hit_or_stand()
                        else:
                            player_response = int(
                                input(
                                    f"\nPlayer: {player.name} - Would you like to hit or stand. (1 -> Hit, 2 -> Stand): "
                                )
                            )
                    except ValueError:
                        print("Invalid. Respond with number 1 or 2.")
                    else:
                        if player_response == Decision.hit:
                            self.hit(player)

                            player_hand_value = player.hand.get_hand_sum()
                            print(f"Current hand value is: {player_hand_value}")

                            if player_hand_value == 21:
                                self.game_winner.append(player)
                                self.end_game(winner=self.game_winner)
                                if player.get_type() == PlayerTypes.Dealer:
                                    print(f"The Dealer has won. Everyone else loses.")
                                else:
                                    print(f"Player {player.get_name()} has won!")
                                game_ended = True
                            elif player_hand_value > 21:
                                if player.get_type() == PlayerTypes.Dealer:
                                    print(f"The Dealer has gone bust!!!")
                                    game_ended = True
                                    for player in self.playing_status:
                                        if player.hand.get_hand_sum() <= 21:
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

    factory: PlayerFactory = PlayerFactory()

    players = [
        factory(PlayerTypes.Normal, "MainCharacterJack"),
        factory(PlayerTypes.Dealer),
        factory(PlayerTypes.Interesting),
        factory(PlayerTypes.Conservative),
        factory(PlayerTypes.PerennialLoser),
    ]

    game_table = Table(players=players)

    game_table.run_game()
