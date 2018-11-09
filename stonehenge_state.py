"""A file defining the current_state of the Stonehenge game.
"""
from typing import Any, List
from copy import deepcopy
from game_state import GameState


class Cell:
    """A class defining a cell.
    =====Attributes======
    cell.id = the identity of the cell. Can carry a str or int
    """

    def __init__(self, identity: Any) -> None:
        """Initializes a cell with ID id.

        @param Cell self: The current cell
        @param identity: The ID of the current cell
        @rtype: None
        """
        self.id = identity


class Leyline:
    """A class defining a Leyline."""

    def __init__(self, cell_list: List['Cell']) -> None:
        """Initializes an object of type 'Leyline'.

        @param Leyline self: the current Leyline
        @param List['Cell']: the list containing all the cells within
        that leyline
        @rtype: None
        """
        self.head = '@'
        self.cell_list = cell_list


class Board:
    """A class defining a board depending on the length of the side.
    ======Attributes=======
    board.horizontal_leylines: a list of horizontal leylines
    board.left_diagonal_leylines: a list of leylines pointing to the
                                  left diagonally
    board.right_diagonal_leylines: a list of leylines pointing to
                                   right diagonally
    board.leyline_tracker: A list of all the leylines of a board.

    """

    def __init__(self, side: int) -> None:
        """initializes a board based on the sidelength side.

        @param Board self: the current board
        @param int side: the integer side length of the board.
        @rtype: None

        >>> g = StonehengeState(3, True)
        >>> g.sidelength == 3
        True
        >>> f = StonehengeState(2, False)
        >>> f.sidelength != 2
        False
        """
        self.horizontal_leylines = []
        self.left_diagonal_leylines = []
        self.right_diagonal_leylines = []
        self.leyline_tracker = []

        if side == 1:
            self.maker_one()

        elif side == 2:
            self.maker_two()

        elif side == 3:
            self.maker_three()

        elif side == 4:
            self.maker_four()

        elif side == 5:
            self.maker_five()

        else:
            print("Invalid length!")

    def maker_one(self) -> None:
        """Creates a playing board of size 1.
        """
        cell1 = Cell('A')
        cell2 = Cell('B')
        cell3 = Cell('C')
        cell4 = Cell('A')
        cell5 = Cell('B')
        cell6 = Cell('C')
        cell7 = Cell('A')
        cell8 = Cell('B')
        cell9 = Cell('C')
        h_leyline1 = Leyline([cell1, cell2])
        h_leyline2 = Leyline([cell3])
        self.horizontal_leylines = [h_leyline1, h_leyline2]
        l_diag_leyline = Leyline([cell4, cell6])
        l_diag_leyline2 = Leyline([cell5])
        self.left_diagonal_leylines = [l_diag_leyline, l_diag_leyline2]
        r_diag_leyline = Leyline([cell8, cell9])
        r_diag_leyline2 = Leyline([cell7])
        self.right_diagonal_leylines = [r_diag_leyline, r_diag_leyline2]
        self.leyline_tracker = [h_leyline1, h_leyline2,
                                l_diag_leyline, l_diag_leyline2,
                                r_diag_leyline2, r_diag_leyline]

    def maker_two(self) -> None:
        """Creates a playing board of size 2.
        """
        cell1, cell2, cell3, cell4, cell5, cell6, cell7 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F'), Cell('G')
        cell8, cell9, cell10, cell11, cell12, cell13, cell14 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F'), Cell('G')
        cell15, cell16, cell17, cell18, cell19, cell20, cell21 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F'), Cell('G')

        h_leyline1 = Leyline([cell1, cell2])
        h_leyline2 = Leyline([cell3, cell4, cell5])
        h_leyline3 = Leyline([cell6, cell7])
        self.horizontal_leylines = [h_leyline1, h_leyline2, h_leyline3]
        l_diag_leyline = Leyline([cell10, cell13])
        l_diag_leyline2 = Leyline([cell8, cell11, cell14])
        l_diag_leyline3 = Leyline([cell9, cell12])
        self.left_diagonal_leylines = [l_diag_leyline, l_diag_leyline2,
                                       l_diag_leyline3]
        r_diag_leyline = Leyline([cell19, cell21])
        r_diag_leyline2 = Leyline([cell16, cell18, cell20])
        r_diag_leyline3 = Leyline([cell15, cell17])
        self.right_diagonal_leylines = [r_diag_leyline, r_diag_leyline2,
                                        r_diag_leyline3]
        self.leyline_tracker = [h_leyline1, h_leyline2,
                                h_leyline3,
                                l_diag_leyline, l_diag_leyline2,
                                l_diag_leyline3, r_diag_leyline2,
                                r_diag_leyline, r_diag_leyline3]

    def maker_three(self) -> None:
        """Creates a playing board of side size 3.
        """
        cell1, cell2, cell3, cell4, cell5, cell6 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F')
        cell7, cell8, cell9, cell10, cell11, cell12 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), \
            Cell('K'), Cell('L')
        cell13, cell14, cell15, cell16, cell17, cell18 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F')
        cell19, cell20, cell21, cell22, cell23, cell24 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), \
            Cell('K'), Cell('L')
        cell25, cell26, cell27, cell28, cell29, cell30 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F')
        cell31, cell32, cell33, cell34, cell35, cell36 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), \
            Cell('K'), Cell('L')

        h_leyline1 = Leyline([cell1, cell2])
        h_leyline2 = Leyline([cell3, cell4, cell5])
        h_leyline3 = Leyline([cell6, cell7, cell8, cell9])
        h_leyline4 = Leyline([cell10, cell11, cell12])
        self.horizontal_leylines = [h_leyline1, h_leyline2, h_leyline3,
                                    h_leyline4]
        l_diag_leyline = Leyline([cell18, cell22])
        l_diag_leyline2 = Leyline([cell15, cell19, cell23])
        l_diag_leyline3 = Leyline([cell13, cell16, cell20, cell24])
        l_diag_leyline4 = Leyline([cell14, cell17, cell21])
        self.left_diagonal_leylines = [l_diag_leyline, l_diag_leyline2,
                                       l_diag_leyline3, l_diag_leyline4]
        r_diag_leyline = Leyline([cell30, cell27, cell25])
        r_diag_leyline2 = Leyline([cell34, cell31, cell28, cell26])
        r_diag_leyline3 = Leyline([cell35, cell32, cell29])
        r_diag_leyline4 = Leyline([cell36, cell33])
        self.right_diagonal_leylines = [r_diag_leyline, r_diag_leyline2,
                                        r_diag_leyline3, r_diag_leyline4]
        self.leyline_tracker = [h_leyline1, h_leyline2,
                                h_leyline3, h_leyline4,
                                l_diag_leyline, l_diag_leyline2,
                                l_diag_leyline3, l_diag_leyline4,
                                r_diag_leyline2, r_diag_leyline,
                                r_diag_leyline3, r_diag_leyline4]

    def maker_four(self) -> None:
        """Creates a playing board of side size 4.
        """
        cell1, cell2, cell3, cell4, cell5, cell6 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), Cell('E'), Cell('F')
        cell7, cell8, cell9, cell10, cell11, cell12 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), Cell('K'), Cell('L')
        cell13, cell14, cell15, cell16, cell17, cell18 = \
            Cell('M'), Cell('N'), Cell('O'), Cell('P'), Cell('Q'), Cell('R')
        cell19, cell20, cell21, cell22, cell23, cell24 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), Cell('E'), Cell('F')
        cell25, cell26, cell27, cell28, cell29, cell30 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), Cell('K'), Cell('L')
        cell31, cell32, cell33, cell34, cell35, cell36 = \
            Cell('M'), Cell('N'), Cell('O'), Cell('P'), Cell('Q'), Cell('R')
        cell37, cell38, cell39, cell40, cell41, cell42 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), Cell('E'), Cell('F')
        cell43, cell44, cell45, cell46, cell47, cell48 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), Cell('K'), Cell('L')
        cell49, cell50, cell51, cell52, cell53, cell54 = \
            Cell('M'), Cell('N'), Cell('O'), Cell('P'), Cell('Q'), Cell('R')

        h_leyline = Leyline([cell1, cell2])
        h_leyline2 = Leyline([cell3, cell4, cell5])
        h_leyline3 = Leyline([cell6, cell7, cell8, cell9])
        h_leyline4 = Leyline([cell10, cell11, cell12, cell13, cell14])
        h_leyline5 = Leyline([cell15, cell16, cell17, cell18])
        self.horizontal_leylines = [h_leyline, h_leyline2, h_leyline3,
                                    h_leyline4, h_leyline5]
        r_diag_leyline = Leyline([cell46, cell42, cell39, cell37])
        r_diag_leyline2 = Leyline([cell51, cell47, cell43, cell40, cell38])
        r_diag_leyline3 = Leyline([cell52, cell48, cell44, cell41])
        r_diag_leyline4 = Leyline([cell53, cell49, cell45])
        r_diag_leyline5 = Leyline([cell54, cell50])
        self.right_diagonal_leylines = [r_diag_leyline, r_diag_leyline2,
                                        r_diag_leyline3, r_diag_leyline4,
                                        r_diag_leyline5]
        l_diag_leyline = Leyline([cell28, cell33])
        l_diag_leyline2 = Leyline([cell24, cell29, cell34])
        l_diag_leyline3 = Leyline([cell21, cell25, cell30, cell35])
        l_diag_leyline4 = Leyline([cell19, cell22, cell26, cell31, cell36])
        l_diag_leyline5 = Leyline([cell20, cell23, cell27, cell32])
        self.left_diagonal_leylines = [l_diag_leyline, l_diag_leyline2,
                                       l_diag_leyline3, l_diag_leyline4,
                                       l_diag_leyline5]
        self.leyline_tracker = [h_leyline, h_leyline2,
                                h_leyline3, h_leyline4, h_leyline5,
                                l_diag_leyline, l_diag_leyline2,
                                l_diag_leyline3, l_diag_leyline4,
                                l_diag_leyline5,
                                r_diag_leyline2, r_diag_leyline,
                                r_diag_leyline3, r_diag_leyline4,
                                r_diag_leyline5]

    def maker_five(self) -> None:
        """Creates a board of side size 5.
        """
        cell1, cell2, cell3, cell4, cell5, cell6 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F')
        cell7, cell8, cell9, cell10, cell11, cell12 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), \
            Cell('K'), Cell('L')
        cell13, cell14, cell15, cell16, cell17, cell18 = \
            Cell('M'), Cell('N'), Cell('O'), Cell('P'), \
            Cell('Q'), Cell('R')
        cell19, cell20, cell21, cell22 = \
            Cell('S'), Cell('T'), Cell('U'), Cell('V')
        cell23, cell24, cell25 = \
            Cell('W'), Cell('X'), Cell('Y')
        cell26, cell27, cell28, cell29, cell30, cell31 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F')
        cell32, cell33, cell34, cell35, cell36, cell37 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), \
            Cell('K'), Cell('L')
        cell38, cell39, cell40, cell41, cell42, cell43 = \
            Cell('M'), Cell('N'), Cell('O'), Cell('P'), \
            Cell('Q'), Cell('R')
        cell44, cell45, cell46, cell47 = \
            Cell('S'), Cell('T'), Cell('U'), Cell('V')
        cell48, cell49, cell50 = \
            Cell('W'), Cell('X'), Cell('Y')
        cell51, cell52, cell53, cell54, cell55, cell56 = \
            Cell('A'), Cell('B'), Cell('C'), Cell('D'), \
            Cell('E'), Cell('F')
        cell57, cell58, cell59, cell60, cell61, cell62 = \
            Cell('G'), Cell('H'), Cell('I'), Cell('J'), \
            Cell('K'), Cell('L')
        cell63, cell64, cell65, cell66, cell67, cell68 = \
            Cell('M'), Cell('N'), Cell('O'), Cell('P'), \
            Cell('Q'), Cell('R')
        cell69, cell70, cell71, cell72 = \
            Cell('S'), Cell('T'), Cell('U'), Cell('V')
        cell73, cell74, cell75 = \
            Cell('W'), Cell('X'), Cell('Y')

        h_leyline = Leyline([cell1, cell2])
        h_leyline2 = Leyline([cell3, cell4, cell5])
        h_leyline3 = Leyline([cell6, cell7, cell8, cell9])
        h_leyline4 = Leyline([cell10, cell11, cell12, cell13, cell14])
        h_leyline5 = Leyline([cell15, cell16, cell17, cell18, cell19, cell20])
        h_leyline6 = Leyline([cell21, cell22, cell23, cell24, cell25])
        self.horizontal_leylines = [h_leyline, h_leyline2, h_leyline3,
                                    h_leyline4, h_leyline5, h_leyline6]
        l_diag_leyline = Leyline([cell40, cell46])
        l_diag_leyline2 = Leyline([cell35, cell41, cell47])
        l_diag_leyline3 = Leyline([cell31, cell36, cell42, cell48])
        l_diag_leyline4 = Leyline([cell28, cell32, cell37, cell43, cell49])
        l_diag_leyline5 = Leyline([cell26, cell29, cell33, cell38,
                                   cell44, cell50])
        l_diag_leyline6 = Leyline([cell27, cell30, cell34, cell39, cell45])
        self.left_diagonal_leylines = [l_diag_leyline, l_diag_leyline2,
                                       l_diag_leyline3, l_diag_leyline4,
                                       l_diag_leyline5, l_diag_leyline6]
        r_diag_leyline = Leyline([cell65, cell60, cell56, cell53, cell51])
        r_diag_leyline2 = Leyline([cell71, cell66, cell61, cell57,
                                   cell54, cell52])
        r_diag_leyline3 = Leyline([cell72, cell67, cell62, cell58, cell55])
        r_diag_leyline4 = Leyline([cell73, cell68, cell63, cell59])
        r_diag_leyline5 = Leyline([cell74, cell69, cell64])
        r_diag_leyline6 = Leyline([cell75, cell70])
        self.right_diagonal_leylines = [r_diag_leyline, r_diag_leyline2,
                                        r_diag_leyline3, r_diag_leyline4,
                                        r_diag_leyline5, r_diag_leyline6]
        self.leyline_tracker = [h_leyline, h_leyline2,
                                h_leyline3, h_leyline4,
                                h_leyline5, h_leyline6,
                                l_diag_leyline, l_diag_leyline2,
                                l_diag_leyline3, l_diag_leyline4,
                                l_diag_leyline5, l_diag_leyline6,
                                r_diag_leyline2, r_diag_leyline,
                                r_diag_leyline3, r_diag_leyline4,
                                r_diag_leyline5, r_diag_leyline6]


class StonehengeState(GameState):
    """A class defining the current state of the Stonehenge
    class and implements methods inherited from GameState.
    =======Attributes======
    StonehengeState.p1_turn: True iff it is p1's turn to make a move
    StonehengeState.sidelength: Side length of the board the game is
                                being played on.
    Stonehenge.board: A board initialized to be the size stated as
                      the Stonehenge State's parameter.
    """

    def __init__(self, sidelength: int, is_p1_turn: bool) -> None:
        """Initializes a current state of a game of Stonehenge.

        @param 'StonehengeState' self: The current state of the current
        game of Stonehenge
        @param int sidelength: The side length of the board of the current
        state of the current game of Stonehenge
        @rtype: None
        """
        self.p1_turn = is_p1_turn
        self.sidelength = sidelength
        self.board = Board(sidelength)

    def __str__(self) -> str:
        """Returnes a user-friendly string representation of the current
        state of the Stonehenge Game.

        """
        if self.sidelength == 1:
            return self.string_creator_1()
        elif self.sidelength == 2:
            return self.string_creator_2()
        elif self.sidelength == 3:
            return self.string_creator_3()
        elif self.sidelength == 4:
            return self.string_creator_4()
        elif self.sidelength == 5:
            return self.string_creator_5()
        return 'Invalid Length'

    def string_creator_1(self) -> str:
        """Returns the grid needed for length 1 boards."""
        a = self.board.left_diagonal_leylines[0].head
        b = self.board.left_diagonal_leylines[1].head
        c = self.board.right_diagonal_leylines[1].head
        d = self.board.right_diagonal_leylines[0].head
        e = self.board.horizontal_leylines[0].head
        f = self.board.horizontal_leylines[0].cell_list[0].id
        g = self.board.horizontal_leylines[0].cell_list[1].id
        h = self.board.horizontal_leylines[1].head
        i = self.board.horizontal_leylines[1].cell_list[0].id

        return """\
                 {}    {}
                /     /     
          {} -- {} -- {} 
               \\   /  \\ 
            {} -- {}     {}
                  \\   
                   {}
        """.format(c, d, e, f, g, h, i, b, a)

    def string_creator_2(self) -> str:
        """Returns a grid needed for length 2 boards of stonehenge."""
        a, b, c, d, e, f = self.board.right_diagonal_leylines[2].head, \
                           self.board.right_diagonal_leylines[1].head, \
                           self.board.horizontal_leylines[0].head, \
                           self.board.horizontal_leylines[0].cell_list[0].id, \
                           self.board.horizontal_leylines[0].cell_list[1].id, \
                           self.board.right_diagonal_leylines[0].head
        g, h, i, j, k, l = self.board.horizontal_leylines[1].head, \
                           self.board.horizontal_leylines[1].cell_list[0].id, \
                           self.board.horizontal_leylines[1].cell_list[1].id, \
                           self.board.horizontal_leylines[1].cell_list[2].id, \
                           self.board.horizontal_leylines[2].head, \
                           self.board.horizontal_leylines[2].cell_list[0].id
        m, n, o, p = self.board.horizontal_leylines[2].cell_list[1].id, \
                     self.board.left_diagonal_leylines[2].head, \
                     self.board.left_diagonal_leylines[0].head, \
                     self.board.left_diagonal_leylines[1].head

        return """
                   {}    {}
                  /     /     
             {} -- {} -- {}    {}
               /  \\  /  \\  /
          {} -- {} -- {} -- {} 
               \\  /  \\  /  \\ 
             {} -- {} -- {}    {}
                 \\     \\ 
                  {}     {}
        """.format(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)

    def string_creator_3(self) -> str:
        """Returns a grid needed for a length 3 stonehenge board."""
        a = self.board.right_diagonal_leylines[0].head
        b = self.board.right_diagonal_leylines[1].head
        c = self.board.horizontal_leylines[0].head
        d = self.board.horizontal_leylines[0].cell_list[0].id
        e = self.board.horizontal_leylines[0].cell_list[1].id
        f = self.board.right_diagonal_leylines[2].head
        g = self.board.horizontal_leylines[1].head
        h = self.board.horizontal_leylines[1].cell_list[0].id
        i = self.board.horizontal_leylines[1].cell_list[1].id
        j = self.board.horizontal_leylines[1].cell_list[2].id
        k = self.board.right_diagonal_leylines[3].head
        l = self.board.horizontal_leylines[2].head
        m = self.board.horizontal_leylines[2].cell_list[0].id
        n = self.board.horizontal_leylines[2].cell_list[1].id
        o = self.board.horizontal_leylines[2].cell_list[2].id
        p = self.board.horizontal_leylines[2].cell_list[3].id
        q = self.board.horizontal_leylines[3].head
        r = self.board.horizontal_leylines[3].cell_list[0].id
        s = self.board.horizontal_leylines[3].cell_list[1].id
        t = self.board.horizontal_leylines[3].cell_list[2].id
        u = self.board.left_diagonal_leylines[3].head
        v = self.board.left_diagonal_leylines[0].head
        w = self.board.left_diagonal_leylines[1].head
        x = self.board.left_diagonal_leylines[2].head

        return """   
                     {}    {}
                    /     /   
            {} --  {} --  {}    {}
                 /  \\ /  \\  /
           {} -- {} -- {} --  {}     {}
              /  \\  /  \\  /  \\  /
         {} -- {} -- {} --  {} --  {} 
              \\   /  \\  /  \\ /  \\
           {} -- {} --  {} --  {}    {}
                 \\     \\    \\
                  {}    {}    {}
        """.format(a, b, c, d, e, f, g, h, i, j, k, l, m, n,
                   o, p, q, r, s, t, u, v, w, x)

    def string_creator_4(self) -> str:
        """Returns a grid needed for a length 4 stonehenge board."""
        a = self.board.right_diagonal_leylines[0].head
        b = self.board.right_diagonal_leylines[1].head
        c = self.board.horizontal_leylines[0].head
        d = self.board.horizontal_leylines[0].cell_list[0].id
        e = self.board.horizontal_leylines[0].cell_list[1].id
        f = self.board.right_diagonal_leylines[2].head
        g = self.board.horizontal_leylines[1].head
        h = self.board.horizontal_leylines[1].cell_list[0].id
        i = self.board.horizontal_leylines[1].cell_list[1].id
        j = self.board.horizontal_leylines[1].cell_list[2].id
        k = self.board.right_diagonal_leylines[3].head
        l = self.board.horizontal_leylines[2].head
        m = self.board.horizontal_leylines[2].cell_list[0].id
        n = self.board.horizontal_leylines[2].cell_list[1].id
        o = self.board.horizontal_leylines[2].cell_list[2].id
        p = self.board.horizontal_leylines[2].cell_list[3].id
        q = self.board.right_diagonal_leylines[4].head
        r = self.board.horizontal_leylines[3].head
        s = self.board.horizontal_leylines[3].cell_list[0].id
        t = self.board.horizontal_leylines[3].cell_list[1].id
        u = self.board.horizontal_leylines[3].cell_list[2].id
        v = self.board.horizontal_leylines[3].cell_list[3].id
        w = self.board.horizontal_leylines[3].cell_list[4].id
        x = self.board.horizontal_leylines[4].head
        y = self.board.horizontal_leylines[4].cell_list[0].id
        z = self.board.horizontal_leylines[4].cell_list[1].id
        aa = self.board.horizontal_leylines[4].cell_list[2].id
        ab = self.board.horizontal_leylines[4].cell_list[3].id
        ac = self.board.left_diagonal_leylines[4].head
        ad = self.board.left_diagonal_leylines[0].head
        ae = self.board.left_diagonal_leylines[1].head
        af = self.board.left_diagonal_leylines[2].head
        ag = self.board.left_diagonal_leylines[3].head

        return """\
                         {}    {}
                        /     / 
                  {} -- {} --  {}     {}
                    /  \\  /  \\  /  
            {} -- {} --- {} ---- {}     {}
                /  \\  /  \\  /   \\  /
          {} -- {} -- {} --- {} ---- {}    {}
            /  \\  /  \\  /  \\  /  \\  /
      {} -- {} -- {} --- {} ---- {} -- {}
            \\  /  \\  /  \\  /  \\  / \\ 
         {} -- {} -- {} -- {} ---  {}    {}
               \\     \\     \\     \\
                {}    {}     {}      {}
    
           
  
             """.format(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o,
                        p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad,
                        ae, af, ag)

    def string_creator_5(self) -> str:
        """Returns a grid needed for a length 5 stonehenge board."""
        a = self.board.right_diagonal_leylines[0].head
        b = self.board.right_diagonal_leylines[1].head
        c = self.board.horizontal_leylines[0].head
        d = self.board.horizontal_leylines[0].cell_list[0].id
        e = self.board.horizontal_leylines[0].cell_list[1].id
        f = self.board.right_diagonal_leylines[2].head
        g = self.board.horizontal_leylines[1].head
        h = self.board.horizontal_leylines[1].cell_list[0].id
        i = self.board.horizontal_leylines[1].cell_list[1].id
        j = self.board.horizontal_leylines[1].cell_list[2].id
        k = self.board.right_diagonal_leylines[3].head
        l = self.board.horizontal_leylines[2].head
        m = self.board.horizontal_leylines[2].cell_list[0].id
        n = self.board.horizontal_leylines[2].cell_list[1].id
        o = self.board.horizontal_leylines[2].cell_list[2].id
        p = self.board.horizontal_leylines[2].cell_list[3].id
        q = self.board.right_diagonal_leylines[4].head
        r = self.board.horizontal_leylines[3].head
        s = self.board.horizontal_leylines[3].cell_list[0].id
        t = self.board.horizontal_leylines[3].cell_list[1].id
        u = self.board.horizontal_leylines[3].cell_list[2].id
        v = self.board.horizontal_leylines[3].cell_list[3].id
        w = self.board.horizontal_leylines[3].cell_list[4].id
        x = self.board.right_diagonal_leylines[5].head
        y = self.board.horizontal_leylines[4].head
        z = self.board.horizontal_leylines[4].cell_list[0].id
        aa = self.board.horizontal_leylines[4].cell_list[1].id
        ab = self.board.horizontal_leylines[4].cell_list[2].id
        ac = self.board.horizontal_leylines[4].cell_list[3].id
        ad = self.board.horizontal_leylines[4].cell_list[4].id
        ae = self.board.horizontal_leylines[4].cell_list[5].id
        af = self.board.horizontal_leylines[5].head
        ag = self.board.horizontal_leylines[5].cell_list[0].id
        ah = self.board.horizontal_leylines[5].cell_list[1].id
        ai = self.board.horizontal_leylines[5].cell_list[2].id
        aj = self.board.horizontal_leylines[5].cell_list[3].id
        ak = self.board.horizontal_leylines[5].cell_list[4].id
        al = self.board.left_diagonal_leylines[5].head
        am = self.board.left_diagonal_leylines[0].head
        an = self.board.left_diagonal_leylines[1].head
        ao = self.board.left_diagonal_leylines[2].head
        ap = self.board.left_diagonal_leylines[3].head
        aq = self.board.left_diagonal_leylines[4].head
        return """\
                         {}    {}
                        /     /    
                  {} --  {} --  {}     {}   
                       / \\   /  \\  /  
                 {} -- {} -- {} --  {}     {}
                    /  \\  /  \\  /  \\  /
              {} -- {} -- {} --  {} --  {}     {}
                 /  \\  /  \\  /  \\  /  \\  / 
           {} -- {} -- {} --  {} --  {} --   {}    {}
              /  \\  /  \\  /  \\  /  \\  /  \\  /
        {} -- {} -- {} --  {} --  {} --  {} --  {}
              \\  /  \\  /  \\  /  \\  /  \\  /  \\
           {} -- {} -- {} --  {} --  {} --  {}     {}
                 \\     \\     \\     \\     \\   
                  {}     {}     {}     {}     {}

              """.format(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q,
                         r, s, t, u, v, w, x, y, z, aa, ab, ac, ad,
                         ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq)

    def get_possible_moves(self) -> List[str]:
        """Returns all the possible moves available to the player.

        @param 'StonehengeState' self: The current state of the curent game
        of Stonehenge
        @rtype: List[str]

        >>> g = StonehengeState(1, True)
        >>> print(g.get_possible_moves())
        ['A', 'B', 'C']
        >>> s = g.make_move('A')
        >>> print(s.get_possible_moves())
        []
        """
        leyline_list = [d.head for d in self.board.leyline_tracker]
        total_length = 3 * int((self.sidelength + 1))
        if leyline_list.count(1) >= total_length / 2 or leyline_list.count(
                2) >= total_length / 2 or '@' not in leyline_list:
            return []
        result = []
        for leyline in self.board.horizontal_leylines:
            for cell in leyline.cell_list:
                if str(cell.id).isalpha():
                    result.append(cell.id)
        return result

    def leyline_head_changer(self, leyline: 'Leyline') -> None:
        """Changes the head value depending on the conditions met
        by the leyline.
        """
        cell_id_list = []
        for cells in leyline.cell_list:
            cell_id_list.append(cells.id)
        numberof1s = cell_id_list.count(1)
        numberof2s = cell_id_list.count(2)
        if numberof1s >= (len(leyline.cell_list) / 2) and leyline.head == '@':
            leyline.head = 1
        elif numberof2s >= (len(leyline.cell_list) / 2) and leyline.head == '@':
            leyline.head = 2

    def make_move(self, move: Any) -> 'StonehengeState':
        """Returns a new current state with the changes made from the previous
        current state after a move is made.
        >>> s = StonehengeState(2, True)
        >>> t = s.make_move('A')
        >>> print(t.get_possible_moves())
        ['B', 'C', 'D', 'E', 'F', 'G']
        """
        newcurrentstate = StonehengeState(self.sidelength, self.p1_turn)
        newcurrentstate.board.horizontal_leylines = \
            self.board.horizontal_leylines[:]
        newcurrentstate.board.left_diagonal_leylines = \
            self.board.left_diagonal_leylines[:]
        newcurrentstate.board.right_diagonal_leylines = \
            self.board.right_diagonal_leylines[:]
        newcurrentstate.board.leyline_tracker = \
            self.board.leyline_tracker[:]
        for leyline in newcurrentstate.board.horizontal_leylines:
            for cell in leyline.cell_list:
                if cell.id == move:
                    cell.id = 1 if newcurrentstate.p1_turn is True else 2
        for l_leylines in newcurrentstate.board.left_diagonal_leylines:
            for cells in l_leylines.cell_list:
                if cells.id == move:
                    cells.id = 1 if newcurrentstate.p1_turn is True else 2
        for r_leylines in newcurrentstate.board.right_diagonal_leylines:
            for cells_d in r_leylines.cell_list:
                if cells_d.id == move:
                    cells_d.id = 1 if newcurrentstate.p1_turn is True else 2
        for leylines in newcurrentstate.board.leyline_tracker:
            newcurrentstate.leyline_head_changer(leylines)
        if self.p1_turn is True:
            newcurrentstate.p1_turn = False
        else:
            newcurrentstate.p1_turn = True
        return newcurrentstate

    def rough_outcome(self: 'StonehengeState') -> int:
        """Returns the probability of winning from a current state.
        >>> s = StonehengeState(1, True)
        >>> t = s.rough_outcome()
        >>> t == 1
        True
        """
        # take the state and check if it is over.
        currentplayer = 'p1' if self.p1_turn else 'p2'
        if self.get_possible_moves() == []:
            if self.get_current_player_name() == currentplayer:
                return -1
            return 1
        singlemovewinlist = []
        masterlist = []
        for g in self.get_possible_moves():
            # check if the children are over
            copy = deepcopy(self)
            newstate = copy.make_move(g)
            if newstate.get_possible_moves() == []:
                if newstate.get_current_player_name() == currentplayer:
                    singlemovewinlist.append(-1)
                else:
                    singlemovewinlist.append(1)
            else:
                insidemovewinlist = []
                for k in newstate.get_possible_moves():
                    # check if the grandchildren are over
                    copycopy = deepcopy(newstate)
                    lateststate = copycopy.make_move(k)
                    if lateststate.get_possible_moves() == []:
                        if lateststate.get_current_player_name() == \
                                currentplayer:
                            insidemovewinlist.append(-1)
                        else:
                            insidemovewinlist.append(1)
                    masterlist.append(insidemovewinlist)
        newsinglemovelist = singlemovewinlist[:]
        newmasterlist = sum(masterlist, [])
        if newsinglemovelist != []:
            return min(newsinglemovelist)
        elif newmasterlist != []:
            return min(newmasterlist)
        return 0

    def __repr__(self):
        """Represent the current state as a string with more
        information than a str method."""
        return self.__str__() + "\n\nThe current player is {}.".format(
            self.get_current_player_name())


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
