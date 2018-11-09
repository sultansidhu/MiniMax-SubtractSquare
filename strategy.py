"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from copy import deepcopy


def interactive_strategy(game: 'Game') -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def recursive_minimax(newgame: 'Game') -> Any:
    """Returns a move that maximizes the chance of computer winning
    and minimizes the change of making a losing move."""
    result = []
    g = {}
    for moves in newgame.current_state.get_possible_moves():
        copy = deepcopy(newgame.current_state)
        newtstate = copy.make_move(moves)
        result.append(newtstate)
    finallist = [newfunction(a) for a in result]
    mini = min(finallist)
    for i in range(len(finallist)):
        if finallist[i] == mini:
            if finallist[i] not in g:
                g[finallist[i]] = []
                g[finallist[i]].append(newgame.current_state.
                                       get_possible_moves()[i])
            else:
                g[finallist[i]].append(newgame.current_state.
                                       get_possible_moves()[i])
    # creates a list of the maximum guaranteed scores
    # of each of the states reachable from the current state.
    return max(g[mini])


def newfunction(state: 'GameState') -> int:
    """Returns the maximum guaranteed score for a given current state.
    """
    cp = 'p1' if state.p1_turn else 'p2'
    op = 'p2' if state.p1_turn else 'p2'
    if state.get_possible_moves() == []:
        if state.get_current_player_name() == cp:
            return -1
        elif state.get_current_player_name() == op:
            return 1
        return 0
    return -1 * min([newfunction(state.make_move(c))
                     for c in state.get_possible_moves()])


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


class Node:
    """A class representing nodes, which link together to form trees.
    ========Attributes========
    Node.cargo = The cargo contained in the node
    Node.children = children of the node
    Node.score = the assigned score to the node
    """

    def __init__(self, cargo) -> None:
        """Initializes a node."""
        self.cargo = cargo
        self.children = None
        self.score = None

    def __str__(self) -> str:
        return "Cargo: {} -- Score: {} -- Children: {}".format(self.cargo, self.score, self.children)


class Stack:
    """ Last-in, first-out (LIFO) stack.

        Note: This stack class has been taken from class lectures.

        ========Attributes=========
        stack._contains: a list of things contained within the stack.
    """

    def __init__(self) -> None:
        """ Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._contains = []

    def add(self, obj: object) -> None:
        """ Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(5)
        """
        self._contains.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not emp.

        # >>> s = Stack()
        # >>> s.add(5)
        # >>> s.add(7)
        # >>> s.remove()
        # 7
        """
        return self._contains.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        return len(self._contains) == 0


def iterative_minimax(game: 'Game') -> Any:
    """An iterative minimax strategy that returns a move that
     maximizes the computer's chance of winning.

    :param game: The game on which we are using the strategy
    :type game: 'Game'
    :return: A move that maximizes the computer's chance to win
    :rtype: Any
    """
    current_state = game.current_state
    current_player = 'p1' if game.current_state.p1_turn else 'p2'
    other = 'p2' if game.current_state.p1_turn else 'p1'
    node = Node(current_state)
    stack = Stack()
    stack.add(node)
    dictionary = {}

    while not stack.is_empty():
        popped_node = stack.remove()
        node_cs = popped_node.cargo
        if len(node_cs.get_possible_moves()) == 0:
            if node_cs.get_current_player_name() == current_player:
                popped_node.score = 1
            elif node_cs.get_current_player_name() == other:
                popped_node.score = 1
            else:
                popped_node.score = 0
        else:
            if popped_node.children is None:
                # means we have not looked at this node yet.
                childrenslist = []
                for moves in popped_node.cargo.get_possible_moves():
                    copy = deepcopy(popped_node.cargo)
                    newstate = copy.make_move(moves)
                    newnode = Node(newstate)
                    childrenslist.append(newnode)
                popped_node.children = childrenslist
                stack.add(popped_node)
                for c in childrenslist:
                    stack.add(c)

            else:
                # means this node has already been looked at.
                scorelist = []
                for kids in popped_node.children:
                    scorelist.append(kids.score * -1)
                maximum = max(scorelist)
                popped_node.score = maximum

    childscores = []
    for z in node.children:
        childscores.append(z.score)
    smallest = max(childscores)
    for i in range(len(childscores)):
        if childscores[i] == smallest:
            if childscores[i] not in dictionary:
                dictionary[childscores[i]] = []
                dictionary[childscores[i]].append(node.cargo.get_possible_moves()[i])
            else:
                dictionary[childscores[i]].append(node.cargo.get_possible_moves()[i])
    return max(dictionary[smallest])


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
