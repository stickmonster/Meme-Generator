"""A meme-creation class using images and quotes.

PILLOW is used to add text to images.
"""
import os
from PIL import Image, ImageDraw, ImageFont
import random

class MemeEngine:
    """A class creating memes from images and quotes."""

    def __init__(self, out_dir:str):
        """The initialisation of class object and creation of out-path."""
        self.out_dir = out_dir
       
        if not os.path.exists(out_dir):
            os.mkdir(self.out_dir)
        self.out_dir = out_dir

    def make_meme(self, file_path = None, body = None, author = None, width = 500) -> str:
        """The compilation of the meme."""
        img = Image.open(file_path)
        w, h = img.size
        width = max(500, width)
        ratio = width/w
        height = int(ratio * h)
        img = img.resize((width, height), Image.NEAREST)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/arial.ttf')
        author = 'by' + f'{author}'
        draw.text((10, 55), author, font = font, fill = 'blue')

        img_out_path = os.path.join(self.out_dir, f'meme_{random.randint(0, 1000000)}.png')

        img.save = img_out_path

        return img_out_path
