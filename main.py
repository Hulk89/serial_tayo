# title: Serial Tayo
# author: Hulk.5
# desc: for geonhoo
# version: 1.1

import pyxel

from srcs.draw_obj import (
    DrawBase,
    Coin,
    TAYO,
    BILLY,
    POKO,
    CHRIS,
    MAX,
    NEW_CAR_1,
    NEW_CAR_2,
    NEW_CAR_3,
    NEW_CAR_4,
    BG_SKY,
    FAR_CLOUD,
    NEAR_CLOUD_1,
    NEAR_CLOUD_2,
    TREE,
    ROAD,
    POLE,
    JUMP,
)

JUMP_CHANNEL=2
COIN_CHANNEL=3
TRANSFORM_SCORE_THR = 50

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
        self.prev_score = 0
        self.player_dy = 0
        self.idx = 0
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
        self.coins = [Coin(i + pyxel.rndi(-5, 5),
                           pyxel.height - 10 + pyxel.rndi(-80, 0))
                        for i in range(100, pyxel.width * 2, 20)]
        self.jumps = generate_objects(JUMP,
                                      y=pyxel.height - JUMP[3] - 2,
                                      step=pyxel.width//3*2)

        self.tayo = DrawBase(72,
                             pyxel.height - TAYO[3] - 2,
                             1,
                             *TAYO)
        
        self.fg_poles = fg_poles

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE) or \
           pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.player_dy = -8
            pyxel.play(JUMP_CHANNEL, 3)
        # NOTE: update player
        self.tayo.y += self.player_dy
        self.player_dy = min(self.player_dy + 1, 8)
        if self.tayo.y < 0:  # NOTE: 벽에 부딪히면...
            self.tayo.y = 0
            self.player_dy = - self.player_dy
            self.score -= 5
            pyxel.play(JUMP_CHANNEL, 4)
        self.tayo.y = min(self.tayo.y,
                          pyxel.height - TAYO[3] - 2)
        
        for jump in self.jumps:
            if self.tayo.is_collision(jump):
                self.player_dy = -12
                pyxel.play(JUMP_CHANNEL, 6)
        
        # NOTE: coin collision detection.
        for coin in self.coins:
            if self.tayo.is_collision(coin):
                self.score += 10
                coin.x = -8  # NOTE: Coin의 width
                pyxel.play(COIN_CHANNEL, 2)
                # NOTE: 100점마다 소리 바꿔주기

                if self.score // TRANSFORM_SCORE_THR > 0 and \
                   (self.score // TRANSFORM_SCORE_THR) > (self.prev_score // TRANSFORM_SCORE_THR):
                    self.prev_score = self.score
                    random_character = [BILLY, POKO, CHRIS, MAX, NEW_CAR_1, NEW_CAR_2, NEW_CAR_3, NEW_CAR_4]
                    char = random_character[self.idx % len(random_character)]
                    self.tayo.img_dict["u"] = char[0]
                    self.tayo.img_dict["v"] = char[1]
                    self.idx += 1
                    self.idx % len(random_character)
                    pyxel.playm(1, loop=False)

        if pyxel.play_pos(0) is None:
            self.tayo.img_dict["u"] = TAYO[0]
            self.tayo.img_dict["v"] = TAYO[1]
            pyxel.playm(0, loop=True)

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
                coin.x += pyxel.width * 2+ pyxel.rndi(-pyxel.width//2, pyxel.width//2)
        for jump in self.jumps:
            jump.x -= 1
            jump.draw()
            if jump.is_hidden():
                jump.x += pyxel.width * 3 + pyxel.rndi(-pyxel.width, pyxel.width)

        self.tayo.draw()

        for pole in self.fg_poles:
            pole.x -= 1
            pole.draw()
            if pole.is_hidden():
                pole.x += pyxel.width * 2
        # NOTE: score
        score_string = f"score : {self.score}"
        pyxel.text(6, 5, score_string, 2)
        pyxel.text(5, 5, score_string, 7)

App()
