import tkinter as tk

class Shogi(tk.Tk):
    def __init__(self):
        super(Shogi, self).__init__()
        self.title("将棋")
        self.geometry("{}x{}+{}+{}".format(400, 500, 500, 100))
        self.resizable(width=0, height=0)

        # {tag: position}
        self.tag2pos = {}
        # 座標からtagの変換
        self.z2tag = {}
        # 符号
        self.numstr = "１２３４５６７８９"
        self.kanstr = "一二三四五六七八九"

        self.set_board()

    def set_board(self):
        self.board = tk.Canvas(self, width=400, height=400, bg="Peach Puff3")
        self.board.pack()

        ### 長方形を作る ###
        # 将棋盤の情報
        # -1 -> 盤の外, 0 -> 空白
        self.board2info = [-1] * 11 + [[0, -1][i in [0, 10]] for i in range(11)] * 9 + [-1] * 11

        for i, y in zip(self.kanstr, range(20, 380, 40)):
            for j, x in zip(self.numstr[::-1], range(20, 380, 40)):
                pos = (x, y, x+40, y+40)
                tag = j + i
                self.tag2pos[tag] = pos[:2]
                self.board.create_rectangle(*pos, fill="Peach Puff3", tags=tag)
                self.z2tag[self.z_coordinate(tag)] = tag
                self.board.tag_bind(tag, "<ButtonPress-1>", self.pressed)
    
    def pressed(self, event):
        item_id = self.board.find_closest(event.x, event.y)
        tag = self.board.gettags(item_id[0])[0]
        print(tag)

    def z_coordinate(self, tag):
        x, y = self.numstr[::-1].index(tag[0])+1, self.kanstr.index(tag[1])+1
        return y*11 + x

    def close(self):
        self.quit()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = Shogi()
    app.run()