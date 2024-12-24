import pyxel

from srcs.draw_obj import (
    DrawBase,
    Coin,
    TAYO,
    BG_SKY,
    FAR_CLOUD,
    NEAR_CLOUD_1,
    NEAR_CLOUD_2,
    TREE,
    ROAD,
    POLE,
)

def generate_objects(object_tuple,
                     y,
                     step,
                     rand_x_range=(0, 0),
                     rand_y_range=(0, 0),
                     scale: float = 1):
    return [DrawBase(i + pyxel.rndi(*rand_x_range),
                     y + pyxel.rndi(*rand_y_range),
                     scale,
                     *object_tuple)
        for i in range(0, pyxel.width * 2, step)]

class App:
    def __init__(self):
        pyxel.init(160, 100, title="Serial Tayo")
        pyxel.load("./assets/tayo.pyxres")

        self.score = 0
        self.player_x = 72
        self.player_y = pyxel.height - TAYO[3]-2
        self.player_dy = 0

        self.setup_env()

        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def setup_env(self):
        far_clouds = generate_objects(FAR_CLOUD,
                                      y=10,
                                      step=FAR_CLOUD[2],
                                      rand_x_range=(-20, 20),
                                      rand_y_range=(-8, 8))
        near_clouds_1 = generate_objects(NEAR_CLOUD_1,
                                         y=30,
                                         step=NEAR_CLOUD_1[2] * 2,
                                         rand_x_range=(-13, 13),
                                         rand_y_range=(-8, 8))
        near_clouds_2 = generate_objects(NEAR_CLOUD_2,
                                         y=30,
                                         step=NEAR_CLOUD_2[2] * 2,
                                         rand_x_range=(-13, 13),
                                         rand_y_range=(-10, 10))
        near_clouds = near_clouds_1 + near_clouds_2
        trees = generate_objects(TREE,
                                 y=pyxel.height - ROAD[3] - TREE[3],
                                 step=TREE[2])
        roads = generate_objects(ROAD,
                                 y=pyxel.height - ROAD[3],
                                 step=ROAD[2])

        bg_poles = generate_objects(POLE,
                                    y=pyxel.height - ROAD[3] - POLE[3],
                                    rand_x_range=(-8, 8),
                                    step=POLE[2] * 3) 
        fg_poles = generate_objects(POLE,
                                    y=pyxel.height - POLE[3],
                                    rand_x_range=(-10, 10),
                                    scale=1.2,
                                    step=POLE[2] * 4) 
        coins = [Coin(100, pyxel.height - 10, 1), Coin(120, pyxel.height - 10, 1)]

        self.bg_sky = generate_objects(BG_SKY,
                                       y=pyxel.height - ROAD[3] - TREE[3] - 10,
                                       step=BG_SKY[2])
        self.continuous_bgs = [
            (16, far_clouds),
            (8, near_clouds),
            (1, trees),
            (1, bg_poles),
            (1, roads),
        ]
        self.coins = coins

        self.tayo = DrawBase(self.player_x, self.player_y, 1, *TAYO)
        
        self.fg_poles = fg_poles

    def update(self):
        pass

    def draw(self):
        pyxel.cls(12)
        for sky in self.bg_sky:
            sky.draw()

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
            if coin.is_hidden():
                coin.x += pyxel.width * 3 + pyxel.rndi(-pyxel.width, pyxel.width)

        self.tayo.draw()

        for pole in self.fg_poles:
            pole.x -= 1
            pole.draw()
            if pole.is_hidden():
                pole.x += pyxel.width * 2


App()
