import pyxel

from srcs.draw_obj import (
        Tayo,
        Road,
        Tree,
        NearCloud1,
        NearCloud2,
        FarCloud,
        Coin,
        Pole,
)

class App:
    def __init__(self):
        pyxel.init(200, 120, title="Serial Tayo", display_scale=3)
        pyxel.load("./assets/tayo.pyxres")

        self.score = 0
        self.player_x = 72
        self.player_y = 100
        self.player_dy = 0
        
        self.coin = Coin(10, 20, 1)
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(12)
        self.coin.draw()
App()
