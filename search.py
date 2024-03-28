from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import draw

font_family = "Anonymous.ttf"

class ResimKaynak():
    def __init__(self, size):
        self.path = "./image.jpg"
        self._size = size
        self.art = None
    
    def ciz(self):
        self.art = draw.IconResim(self.path, self._size)
        self.art.art()

    def duzelt(self, thresold):
        self.art.thresold = thresold
        self.ciz()
        self.art.thresold = 1

    def reverse_color(self):
        draw.Resim.trans_renk()
        self.ciz()
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def set_size(self, deger):
        if deger < 7:
            print("o kadar da değil")
        else:
            self._size = (deger, deger)
            self.ciz()
    
class Icon(ResimKaynak):
    def __init__(self, query, size = (25,25)):
        super().__init__(size)
        self.query = query + "-icon"
        self._index = 0
        self.image_url = None
        self.image_list = []
        try:
            self.get_image_urls()
            self.get_image()
        except ConnectionError as e:
            print(e)

    def get_image_urls(self):
        try:
            if not self.image_url:
                response = requests.get("https://www.google.com/search?q=" + self.query + "&tbm=isch")
                soup = BeautifulSoup(response.content, "html.parser")
                self.image_list = [x for x in soup.find_all("img")]
        except:
            raise ConnectionError("internet bağlantısını kontrol et")

    def set_url(self):
        self.image_url = self.image_list[self._index].get("src")

    def get_url(self):
        return self.image_url

    def get_image(self):
 
        try:
            url = self.get_url()
            urlretrieve(url, "image.jpg")
            self.ciz()
        except TypeError:
            self.resim_degis() 
    
    def resim_degis(self):
        if self._index < len(self.image_list) - 1 :
            self._index += 1
            self.set_url()
            return self.get_image()
        else:
            print("bulamadım")


class Text(ResimKaynak):
    fonts_path = "./fonts/"
    def __init__(self, text):
        self.text = text if len(text)%12 == 0 else text[:12] + "\n" + text[12:]
        self.out_height = self.text.count("\n") + 1
        self.out_width = 60
        super().__init__((80, self.out_height * 10))

        self.image_width = self.out_width * 4
        self.image_height = self.out_height * 25
        self.img = Image.new("RGB", (self.image_width, self.image_height), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.img)

        self.text_olustur()
    
    def ciz(self):
        self.art = draw.TextResim(self.path, self._size)
        self.art.trans_renk()
        self.art.art()
        

    def text_olustur(self):
        font = ImageFont.truetype( self.fonts_path + font_family, size=25)
        self.draw.text((0,0), self.text, fill=(0, 0, 0), font=font)
        self.img.save("image.jpg")
        self.ciz()
