from PIL import Image, ImageDraw
from flask import Flask, request


class LabeledImage:
    def __init__(self, image_path, Label=None):
        self.image = Image.open(image_path)
        self.image_name = image_path
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.label = Label
        self.pix = self.image.load()
        self.pix_array = list()

    def detect_Bounding_Coordinates(self):
        for x in range(self.width):
            for y in range(self.height):
                if sum(self.pix[x, y]) != 765:
                    self.pix_array.append((x, y))
        return (self.pix_array[0][0], self.pix_array[0][1] // 3), (self.pix_array[-1][0], self.pix_array[-1][1] * 1.45)

    def draw(self):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle(
            (self.pix_array[0][0], self.pix_array[0][1] // 3, self.pix_array[-1][0], self.pix_array[-1][1] * 1.45),
            outline=(255, 0, 0))
        self.image.save(f'detect_{self.image_name}')



