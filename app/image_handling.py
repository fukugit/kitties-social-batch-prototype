import base64
import os

class ImageHandling:

    # 画像をencode
    @staticmethod
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # default フォルダの直下にある画像を全部取得．default は"./images"
    @staticmethod
    def get_all_images():
        return os.listdir("./images")

    # ./imagesの直下にある画像を指定して取得
    @staticmethod
    def get_specify_image_path(image_name):
        return f"./images/{image_name}"