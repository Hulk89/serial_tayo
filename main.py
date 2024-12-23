import pyxel

from srcs.draw_obj import (
    DrawBase,
    Coin,
    TAYO,
    FAR_CLOUD,
    NEAR_CLOUD_1,
    NEAR_CLOUD_2,
    TREE,
    ROAD,
    POLE,
)


class App:
    def __init__(self):
        pyxel.init(160, 100, title="Serial Tayo")
        pyxel.load("./assets/tayo.pyxres")

        self.score = 0
        self.player_dy = 0

        self.setup_env()

        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def setup_env(self):
        far_clouds = [
            DrawBase(i + pyxel.rndi(-20, 20), 10 + pyxel.rndi(-8, 8), 1, *FAR_CLOUD)
            for i in range(0, pyxel.width * 2, FAR_CLOUD[2])
        ]
        near_clouds = [
            DrawBase(
                i + pyxel.rndi(-13, 13), 20 + pyxel.rndi(-8, 8), 1.3, *NEAR_CLOUD_1
            )
            for i in range(0, pyxel.width * 2, int(NEAR_CLOUD_1[2] * 1.3))
        ]
        trees = [
            DrawBase(i, pyxel.height - ROAD[3] - TREE[3], 1, *TREE)
            for i in range(0, pyxel.width * 2, TREE[2])
        ]
        roads = [
            DrawBase(i, pyxel.height - ROAD[3], 1, *ROAD)
            for i in range(0, pyxel.width * 2, ROAD[2])
        ]
        bg_poles = [
            DrawBase(i + pyxel.rndi(-8, 8), pyxel.height - ROAD[3] - POLE[3], 1, *POLE)
            for i in range(0, pyxel.width * 2, POLE[2] * 3)
        ]
        fg_poles = [
            DrawBase(i + pyxel.rndi(-10, 10), pyxel.height - POLE[3], 1.2, *POLE)
            for i in range(0, pyxel.width * 2, POLE[2] * 4)
        ]
        coins = [Coin(100, 92, 1), Coin(120, 92, 1)]

        self.continuous_bgs = [
            (16, far_clouds),
            (8, near_clouds),
            (1, trees),
            (1, bg_poles),
            (1, roads),
        ]
        self.coins = coins

        self.player_x = 72
        self.player_y = pyxel.height - TAYO[3]-2
        self.tayo = DrawBase(self.player_x, self.player_y, 1, *TAYO)
        
        self.fg_poles = fg_poles

    def update(self):
        pass

    def draw(self):
        pyxel.cls(12)

        for dinom, bg in self.continuous_bgs:
            for item in bg:
                if (pyxel.frame_count % dinom) == 0:
                    item.x -= 1
                item.draw()
                if item.is_hidden():
                    item.x += pyxel.width * 2
        for coin in self.coins:
            coin.x -= 1
            coin.draw()

        self.tayo.draw()

        for pole in self.fg_poles:
            pole.x -= 1
            pole.draw()
            if pole.is_hidden():
                pole.x += pyxel.width * 2


App()
