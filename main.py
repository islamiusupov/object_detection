from yolotrainer import  LabeledImageFactory
import sys
from flask import Flask

app = Flask(__name__)


class YoloBoxBackend:
    @app.route('/1')
    def upload_labeled_image(self, params):
        return f'<h1>OK<h1>'


path = sys.stdin.readline().strip()
color = sum(map(int, input().split()))
test = LabeledImageFactory.generate_labeled_image(path, color)
test1 = YoloBoxBackend()
test1.upload_labeled_image(test.upload_to_server('localhost', 3000))


if __name__ == "__main__":
    app.run(debug=True)
