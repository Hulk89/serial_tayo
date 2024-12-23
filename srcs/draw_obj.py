import pyxel

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

class Tayo(DrawBase):
    def __init__(self, x, y, scale):
        super().init(x, y, scale, 0, 0, 16, 8)

class Rani(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 0, 8, 16, 8)

class Gani(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 16, 0, 16, 8)

class Rogy(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 16, 8, 16, 8)

class FarCloud(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 0, 16, 14, 5)

class NearCloud1(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 0, 24, 20, 8)

class NearCloud2(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 25, 24, 16, 8)

class Tree(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 32, 0, 32, 8)

class Road(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 40, 0, 32, 8)

class Pole(DrawBase):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 48, 8, 16, 8)


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
