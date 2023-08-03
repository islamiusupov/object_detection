from PIL import Image, ImageDraw



class LabeledImage:
    def __init__(self, image_path, color, label=None):
        self.image = Image.open(image_path)
        self.image_name = image_path
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.color = color
        self.pix = self.image.load()
        self.pix_array = list()
        self.label = label

    def detect_Bounding_Coordinates(self):
        for x in range(self.width):
            for y in range(self.height):
                if sum(self.pix[x, y]) != self.color:
                    self.pix_array.append((x, y))
        return (self.pix_array[0][0], self.pix_array[0][1] // 3), (self.pix_array[-1][0], self.pix_array[-1][1] * 1.45)

    def draw(self):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle(
            (self.pix_array[0][0], self.pix_array[0][1] // 3, self.pix_array[-1][0], self.pix_array[-1][1] * 1.45),
            outline=(255, 0, 0))
        self.image.save(f'detect_{self.image_name}')

    def upload_to_server(self, server_host, server_port):
        for x in range(self.width):
            for y in range(self.height):
                if sum(self.pix[x, y]) != self.color:
                    self.pix_array.append((x, y))
        json = {
            'file_content': self.image_name,
            'label': self.label,
            'bound_start_x': self.pix_array[0][0],
            'bound_start_y': self.pix_array[0][1] // 3,
            'bound_end_x': self.pix_array[-1][0],
            'bound_end_y': self.pix_array[-1][1] * 1.45
           }
        return json, server_host, server_port


class LabeledImageFactory:
    @staticmethod
    def generate_labeled_image(file_path, bg_color, label=None):
        return LabeledImage(file_path, bg_color, label)
