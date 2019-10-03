# coding: utf-8

X = 0   # Cannot Move
O = 1   # Move
L = 2   # Linear Move
J = 3   # Jump

class Piece(object):
    EMPTY = -1
    FIRST_PLAYER = 0
    SECOND_PLAYER = 1

    def __init__(self, name, owner, move_vec):
        self._name = name
        self._owner = owner
        self._move_vec = move_vec

    @property
    def name(self):
        return self._name

    @property
    def owner(self):
        return self._owner

    @property
    def angle(self):
        if self._owner == self.FIRST_PLAYER:
            return 0
        else:
            return 180
    
    @property
    def is_empty(self):
        if self.owner == self.EMPTY:
            return True
        return False
    
    def is_enemy_of(self, attacker):
        if attacker.owner == self.FIRST_PLAYER or attacker.owner == self.SECOND_PLAYER:
            if attacker.owner != self.owner:
                return True
        return False

    @staticmethod
    def get_movable_map(pieces, i, j, turn):
        piece = pieces[j][i]
        movable_map = [[0 for _ in range(9)] for _ in range(9)]
        if piece.owner != turn:
            return movable_map
        direction = 0
        if piece.owner == Piece.FIRST_PLAYER:
            direction = -1
        if piece.owner == Piece.SECOND_PLAYER:
            direction = 1
        for dy, row in enumerate(piece._move_vec):
            for dx, col in enumerate(row):
                x = i + (dx - 1) * direction
                y = j + (2 - dy) * direction
                if not (x >= 0 and x < 9 and y >= 0 and y < 9):
                    continue
                if col == X:
                    movable_map[y][x] = 0
                if col == O:
                    if pieces[y][x].is_empty or pieces[y][x].is_enemy_of(piece):
                        movable_map[y][x] = 1
                if col == L:
                    while True:
                        if pieces[y][x].is_empty:
                            movable_map[y][x] = 1
                            x += (dx - 1) * direction
                            y += (2 - dy) * direction
                            if not (x >= 0 and x < 9 and y >= 0 and y < 9):
                                break
                        elif pieces[y][x].is_enemy_of(piece):
                            movable_map[y][x] = 1
                            break
                        else:
                            break
                if col == J:
                    if pieces[y][x].is_empty or pieces[y][x].is_enemy_of(piece):
                        movable_map[y][x] = 1
        return movable_map

class Empty(Piece):
    def __init__(self):
        super(Empty, self).__init__("", Piece.EMPTY,
            move_vec=[
                [X, X, X],
                [X, X, X],
                [X, X, X],
                [X, X, X]
            ]
        )

class Fu(Piece):
    def __init__(self, owner):
        super(Fu, self).__init__("歩", owner,
            move_vec=[
                [X, X, X],
                [X, O, X],
                [X, X, X],
                [X, X, X]
            ]
        )

class To(Piece):
    def __init__(self, owner):
        super(To, self).__init__("と", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [O, X, O],
                [X, O, X]
            ]
        )

class Kyo(Piece):
    def __init__(self, owner):
        super(Kyo, self).__init__("香", owner,
            move_vec=[
                [X, X, X],
                [X, L, X],
                [X, X, X],
                [X, X, X]
            ]
        )

class NariKyo(Piece):
    def __init__(self, owner):
        super(NariKyo, self).__init__("杏", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [O, X, O],
                [X, O, X]
            ]
        )

class Kei(Piece):
    def __init__(self, owner):
        super(Kei, self).__init__("桂", owner,
            move_vec=[
                [J, X, J],
                [X, X, X],
                [X, X, X],
                [X, X, X]
            ]
        )

class NariKei(Piece):
    def __init__(self, owner):
        super(NariKei, self).__init__("圭", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [O, X, O],
                [X, O, X]
            ]
        )

class Gin(Piece):
    def __init__(self, owner):
        super(Gin, self).__init__("銀", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [X, X, X],
                [O, X, O]
            ]
        )

class NariGin(Piece):
    def __init__(self, owner):
        super(NariGin, self).__init__("全", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [O, X, O],
                [X, O, X]
            ]
        )

class Kin(Piece):
    def __init__(self, owner):
        super(Kin, self).__init__("金", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [O, X, O],
                [X, O, X]
            ]
        )

class Kaku(Piece):
    def __init__(self, owner):
        super(Kaku, self).__init__("角", owner,
            move_vec=[
                [X, X, X],
                [L, X, L],
                [X, X, X],
                [L, X, L]
            ]
        )

class Uma(Piece):
    def __init__(self, owner):
        super(Uma, self).__init__("馬", owner,
            move_vec=[
                [X, X, X],
                [L, O, L],
                [O, X, O],
                [L, O, L]
            ]
        )

class Hisha(Piece):
    def __init__(self, owner):
        super(Hisha, self).__init__("飛", owner,
            move_vec=[
                [X, X, X],
                [X, L, X],
                [L, X, L],
                [X, L, X]
            ]
        )

class Ryu(Piece):
    def __init__(self, owner):
        super(Ryu, self).__init__("龍", owner,
            move_vec=[
                [X, X, X],
                [O, L, O],
                [L, X, L],
                [O, L, O]
            ]
        )

class Ou(Piece):
    def __init__(self, owner):
        super(Ou, self).__init__("王", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [O, X, O],
                [O, O, O]
            ]
        )

class Gyoku(Piece):
    def __init__(self, owner):
        super(Gyoku, self).__init__("玉", owner,
            move_vec=[
                [X, X, X],
                [O, O, O],
                [O, X, O],
                [O, O, O]
            ]
        )