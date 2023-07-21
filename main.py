from yolotrainer import LabeledImage
import sys


class LabeledImageFactory:
    @staticmethod
    def generate_labeled_image(file_path, Label=None):
        return LabeledImage(file_path)


path = sys.stdin.readline().strip()
test = LabeledImageFactory.generate_labeled_image(path)
print(test.detect_Bounding_Coordinates())
test.draw()
