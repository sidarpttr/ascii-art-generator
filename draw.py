from PIL import Image

class Resim:
    siyah = " "
    beyaz = "*"
    def __init__(self, path, size, thresold=1):
        self.size = size
        self.image = Image.open(path)
        self.thresold = thresold
        self.bw_image = self.image.convert("L").resize(self.size)

    def art(self):
        pixels = self.bw_image.load()
        bw_array = [[0 for _ in range(self.bw_image.width)] for _ in range(self.bw_image.height)]

        for y in range(self.bw_image.height):
            for x in range(self.bw_image.width):
                bw_array[y][x] = 0 if pixels[x,y] < self.thresold else 1

        for row in bw_array:
            print(' '.join(map(lambda x: Resim.beyaz if not x else Resim.siyah, row)))
    
    @classmethod
    def trans_renk(cls):
        cls.beyaz = "*" if cls.beyaz == " " else " "
        cls.siyah = " " if cls.siyah == "*" else "*"

class IconResim(Resim):
    def __init__(self, path, size, thresold=128):
        super().__init__(path, size, thresold=thresold)
    
class TextResim(Resim):
    def __init__(self, path, size, thresold=156):
        super().__init__(path, size, thresold=thresold)
