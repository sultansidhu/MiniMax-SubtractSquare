"""A file representing the class Stonehenge, which is
subclass of Game, and the implementation of its functions.
"""
from game import Game
from stonehenge_state import StonehengeState
from typing import Any


class StonehengeGame(Game):
    """A class representing the game of Stonehenge, inheriting
    from Game and implementing all its methods.
    """

    def __init__(self, p1_starts):
        """Initializes a game of Stonehenge with side length
        side_length.

        @param 'StonehengeGame' self: The current game of Stonehenge
        @param bool p1_starts: boolean dictating if p1 starts.
        @rtype: None
        """
        self.side_length = input("What would you like the length " +
                                 "of your board to be?")
        self.p1_starts = p1_starts
        self.current_state = StonehengeState(int(self.side_length), p1_starts)

    def get_instructions(self):
        """Returns a string containing the instructions on how to
        play the game.
        """
        return "The game is played by each of the two players claiming " \
               "a cell, which then changes from representing an alphabet" \
               "to representing the number of the player that captured it." \
               "When more than half the cells in a line have been claimed" \
               "by a single user, the ley-line is claimed by the " \
               "user completely." \
               "when more than half the ley-lines have been claimed by " \
               "a player, the player wins."

    def is_over(self, currentstate: 'GameState') -> bool:
        """Returns True iff according to the current_state, the game ends.

        @param 'StonehengeGame' self: the current game of Stonehenge
        @param Any currentstate: the current state of the game of Stonehenge
        @rtype: bool

        """
        leyline_list = [d.head for d in currentstate.board.leyline_tracker]
        total_length = 3 * (int(self.side_length) + 1)
        if leyline_list.count(1) >= total_length / 2:
            return True
        elif leyline_list.count(2) >= total_length / 2:
            return True
        elif '@' not in leyline_list:
            return True
        return False

    def is_winner(self, player: str):
        """Returns True if the player player is the winner of the game.

        @param 'StonehengeGame' self: The current game of Stonehenge
        @param str player: the player being entered to check if
                           he/she is the winner.
        @rtype: bool
        """
        headlist = [c.head for c in self.current_state.board.leyline_tracker]
        if player == 'p1':
            if headlist.count(1) >= len(headlist)/2:
                # checks if the number of leylines claimed by p1 is more than
                # half the number of total leylines
                return True
            elif "@" not in headlist and headlist.count(1) > headlist.count(2):
                # checks that if all leylines are claimed, then the ones claimed
                # by p1 are more than the ones claimed by p2
                return True
            return False
        elif player == 'p2':
            if headlist.count(2) >= len(headlist)/2:
                # checks if the number of leylines claimed by p2 is more than
                # half the number of total leylines
                return True
            elif "@" not in headlist and headlist.count(2) > headlist.count(1):
                # checks that if all leylines are claimed, then the ones claimed
                # by p2 are more than the ones claimed by p1
                return True
            return False
        return False

    def str_to_move(self, move: str) -> Any:
        """Returns a valid move based on the inputted string. If the inputted
        string represents an invalid move, return an invalid move.

        @param 'StonehengeGame' self: The current game of Stonehenge
        @param str move: The entered string representing a valid
                         or an invalid move
        @rtype: Any
        """
        if move.upper() in self.current_state.get_possible_moves():
            return move.upper()


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
