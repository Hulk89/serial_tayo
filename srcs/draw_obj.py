import pyxel


TAYO = (0, 0, 16, 8)
CHRIS = (0, 8, 16, 8)
BILLY = (16, 0, 16, 8)
POKO = (16, 8, 16, 8)

FAR_CLOUD = (0, 16, 14, 5)
NEAR_CLOUD_1 = (0, 24, 20, 8)
NEAR_CLOUD_2 = (25, 24, 16, 8)
TREE = (0, 32, 32, 8)
ROAD = (0, 40, 32, 8)
POLE = (48, 8, 16, 8)
BG_SKY = (48, 32, 16, 16)

JUMP = (32, 8, 8, 8)

class DrawBase:
    def __init__(self, x, y, scale, u, v, w, h, img=0):
        self.img_dict = {
            "u": u,
            "v": v,
            "w": w,
            "h": h,
            "img": img,
            "colkey": 2,
        }
        self.x = x
        self.y = y
        self.scale = scale

    def draw(self):
        pyxel.blt(self.x,
                  self.y,
                  scale=self.scale,
                  **self.img_dict)

    def __len__(self):
        return self.img_dict["w"]

    def is_hidden(self):
        return self.x < -len(self)

    @property
    def w(self):
        return self.img_dict["w"]

    @property
    def h(self):
        return self.img_dict["h"]

    def is_collision(self, o):
        horizontal_overlap = (self.x < o.x + o.w) and (self.x + self.w > o.x)
        vertical_overlap = (self.y < o.y + o.h) and (self.y + self.h > o.y)
    
        return horizontal_overlap and vertical_overlap


class Coin(DrawBase):
    def __init__(self, x, y, scale=1):
        super().__init__(x, y, scale, 32, 0, 8, 8)
        
    def draw(self):
        # NOTE: Animation
        img_dict = self.img_dict.copy()
        img_dict["u"] += (pyxel.frame_count // 4) % 2 * 8

        pyxel.blt(self.x,
                  self.y,
                  scale=self.scale,
                  **img_dict)
