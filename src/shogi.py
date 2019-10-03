# coding: utf-8

import tkinter as tk
import pieces

class Shogi(tk.Tk):
    def __init__(self):
        super(Shogi, self).__init__()
        self.title("将棋")
        self.geometry("{}x{}+{}+{}".format(400, 500, 500, 100))
        self.resizable(width=0, height=0)

        # {tag: position}
        self._tag2pos = {}
        # 座標からtagの変換
        self._z2tag = {}
        # 符号
        self._numstr = "１２３４５６７８９"
        self._kanstr = "一二三四五六七八九"

        self.set_board()
        self.set_bind()
        self.init()

    def set_board(self):
        self._board = tk.Canvas(self, width=400, height=400, bg="Peach Puff3")
        self._board.pack()

        ### 長方形を作る ###
        # 将棋盤の情報
        # -1 -> 盤の外, 0 -> 空白
        self._board2info = [-1] * 11 + [[0, -1][i in [0, 10]] for i in range(11)] * 9 + [-1] * 11

        for i, y in zip(self._kanstr, range(20, 380, 40)):
            for j, x in zip(self._numstr[::-1], range(20, 380, 40)):
                pos = (x, y, x+40, y+40)
                tag = j + i
                self._tag2pos[tag] = pos[:2]
                self._board.create_rectangle(*pos, fill="Peach Puff3", tags=tag)
                self._z2tag[self.z_coordinate(tag)] = tag

    def set_bind(self):
        for tag in self._tag2pos.keys():
            self._board.tag_bind(tag, "<ButtonPress-1>", self.pressed)
    
    def pressed(self, event):
        for tag in self._tag2pos.keys():
            self._board.itemconfig(tag, fill="Peach Puff3")
        item_id = self._board.find_closest(event.x, event.y)
        tag = self._board.gettags(item_id[0])[0]
        i, j = self.get_index(tag)
        piece = self.get_piece(tag)
        piece2 = self.get_piece("９一")
        print(tag, piece.name)
        print(piece2.is_enemy_of(piece))
        movable_map = pieces.Piece.get_movable_map(self._pieces, i, j, pieces.Piece.SECOND_PLAYER)
        for j, row in enumerate(movable_map):
            for i, col in enumerate(row):
                print(col)
                if col == 1:
                    print(i, j)
                    tag = self.get_tag(i, j)
                    self._board.itemconfig(tag, fill="orange red")
        self.update_board()

    def z_coordinate(self, tag):
        x, y = self._numstr[::-1].index(tag[0])+1, self._kanstr.index(tag[1])+1
        return y*11 + x

    def get_index(self, tag):
        x, y = self._tag2pos[tag]
        i = (x - 20) // 40
        j = (y - 20) // 40
        return i, j

    def get_tag(self, i, j):
        z = ((j + 1) * 11) + (i + 1)
        tag = self._z2tag[z]
        return tag

    def get_piece(self, tag):
        x, y = self._tag2pos[tag]
        i = (x - 20) // 40
        j = (y - 20) // 40
        return self._pieces[j][i]
    
    def init(self):
        empty = pieces.Empty()

        fFu = pieces.Fu(owner=pieces.Piece.FIRST_PLAYER)
        fKyo = pieces.Kyo(owner=pieces.Piece.FIRST_PLAYER)
        fKei = pieces.Kei(owner=pieces.Piece.FIRST_PLAYER)
        fGin = pieces.Gin(owner=pieces.Piece.FIRST_PLAYER)
        fKin = pieces.Kin(owner=pieces.Piece.FIRST_PLAYER)
        fKaku = pieces.Kaku(owner=pieces.Piece.FIRST_PLAYER)
        fHisha = pieces.Hisha(owner=pieces.Piece.FIRST_PLAYER)
        fGyoku = pieces.Gyoku(owner=pieces.Piece.FIRST_PLAYER)

        sFu = pieces.Fu(owner=pieces.Piece.SECOND_PLAYER)
        sKyo = pieces.Kyo(owner=pieces.Piece.SECOND_PLAYER)
        sKei = pieces.Kei(owner=pieces.Piece.SECOND_PLAYER)
        sGin = pieces.Gin(owner=pieces.Piece.SECOND_PLAYER)
        sKin = pieces.Kin(owner=pieces.Piece.SECOND_PLAYER)
        sKaku = pieces.Kaku(owner=pieces.Piece.SECOND_PLAYER)
        sHisha = pieces.Hisha(owner=pieces.Piece.SECOND_PLAYER)
        sOu = pieces.Ou(owner=pieces.Piece.SECOND_PLAYER)

        self._pieces = [
            [sKyo,  sKei,   sGin,   sKin,   sOu,    sKin,   sGin,   sKei,   sKyo ],
            [empty, sHisha, empty,  empty,  empty,  empty,  empty,  sKaku,  empty],
            [sFu,   sFu,    sFu,    sFu,    sFu,    sFu,    sFu,    sFu,    sFu  ],
            [empty, empty,  empty,  empty,  empty,  empty,  empty,  empty,  empty],
            [empty, empty,  empty,  empty,  empty,  empty,  empty,  empty,  empty],
            [empty, empty,  empty,  empty,  empty,  empty,  empty,  empty,  empty],
            [fFu,   fFu,    fFu,    fFu,    fFu,    fFu,    fFu,    fFu,    fFu  ],
            [empty, fKaku,  empty,  empty,  empty,  empty,  empty,  fHisha, empty],
            [fKyo,  fKei,   fGin,   fKin,   fGyoku, fKin,   fGin,   fKei,   fKyo ]
        ]

        self.update_board()

    def update_board(self):
        for i, row in enumerate(self._pieces):
            for j, piece in enumerate(row):
                tag = self._numstr[9-(j+1)] + self._kanstr[i]
                x, y = self._tag2pos[tag]
                print(piece.name)
                self._board.create_text(
                    x+20, y+20,
                    font=("Meiryo", 18, "bold"),
                    angle=piece.angle,
                    text=piece.name,
                    tags=self._z2tag[self.z_coordinate(tag)]
                )

    def close(self):
        self.quit()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = Shogi()
    app.run()