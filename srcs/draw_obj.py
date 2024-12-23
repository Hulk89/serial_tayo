import pyxel


TAYO = (0, 0, 16, 8)
RANI = (0, 8, 16, 8)
GANI = (16, 0, 16, 8)
ROGY = (16, 8, 16, 8)
FAR_CLOUD = (0, 16, 14, 5)
NEAR_CLOUD_1 = (0, 24, 20, 8)
NEAR_CLOUD_2 = (25, 24, 16, 8)
TREE = (0, 32, 32, 8)
ROAD = (0, 40, 32, 8)
POLE = (48, 8, 16, 8)


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

class Coin(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 32, 0, 8, 8)
        
    def draw(self):
        # NOTE: Animation
        img_dict = self.img_dict.copy()
        img_dict["u"] += (pyxel.frame_count // 4) % 2 * 8

        pyxel.blt(self.x,
                  self.y,
                  scale=self.scale,
                  **img_dict)
