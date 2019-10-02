# coding: utf-8

class Piece(object):
    EMPTY = -1
    FIRST_PLAYER = 0
    SECOND_PLAYER = 1

    def __init__(self, name, owner):
        self._name = name
        self._owner = owner
    
    @property
    def name(self):
        return self._name

    @property
    def angle(self):
        if self._owner == self.FIRST_PLAYER:
            return 0
        else:
            return 180

class Empty(Piece):
    def __init__(self):
        super(Empty, self).__init__("", Piece.EMPTY)

class Fu(Piece):
    def __init__(self, owner):
        super(Fu, self).__init__("歩", owner)

class To(Piece):
    def __init__(self, owner):
        super(To, self).__init__("と", owner)

class Kyo(Piece):
    def __init__(self, owner):
        super(Kyo, self).__init__("香", owner)

class NariKyo(Piece):
    def __init__(self, owner):
        super(NariKyo, self).__init__("杏", owner)

class Kei(Piece):
    def __init__(self, owner):
        super(Kei, self).__init__("桂", owner)

class NariKei(Piece):
    def __init__(self, owner):
        super(NariKei, self).__init__("圭", owner)

class Gin(Piece):
    def __init__(self, owner):
        super(Gin, self).__init__("銀", owner)

class NariGin(Piece):
    def __init__(self, owner):
        super(NariGin, self).__init__("全", owner)

class Kin(Piece):
    def __init__(self, owner):
        super(Kin, self).__init__("金", owner)

class Kaku(Piece):
    def __init__(self, owner):
        super(Kaku, self).__init__("角", owner)

class Uma(Piece):
    def __init__(self, owner):
        super(Uma, self).__init__("馬", owner)

class Hisha(Piece):
    def __init__(self, owner):
        super(Hisha, self).__init__("飛", owner)

class Ryu(Piece):
    def __init__(self, owner):
        super(Ryu, self).__init__("龍", owner)

class Ou(Piece):
    def __init__(self, owner):
        super(Ou, self).__init__("王", owner)

class Gyoku(Piece):
    def __init__(self, owner):
        super(Gyoku, self).__init__("玉", owner)