from model.cat import Cats
from csv_handling import CsvHandling
from openai_request_handling import OpenaiRequestHandling
from organization_prompt_handling.base_prompt import BasePrompt
from image_handling import ImageHandling
from tqdm import tqdm
import time

images = ImageHandling.get_all_images()
system_prompt = BasePrompt.create_system_prompt()

# 各血統書に保存した猫の情報リスト
cat_info = []

client = OpenaiRequestHandling("gpt-4o-2024-11-20")

for image in tqdm(images, desc="画像処理中"):
    user_prompt = BasePrompt.create_user_prompt(image)
    start_time = time.time()
    completion = client.get_response(0.05, Cats, system_prompt, user_prompt)
    cat_info.append(completion.choices[0].message.parsed)
    elapsed_time = time.time() - start_time
    tqdm.write(f"画像 {images.index(image) + 1}/{len(images)} 処理完了 (所要時間: {elapsed_time:.2f}秒)")

# csv header のリスト
fieldnames = [
    "no",
    "name",
    "breed",
    "sex",
    "eye_color",
    "color",
    "date_of_birth",
    "registration_number",
    "breeder",
    "owner",
    "date_of_registration"]

for i in tqdm(range(len(cat_info)), desc="CSV出力中"):
    file_name = CsvHandling.get_csv_file_name(images[i])
    start_time = time.time()
    CsvHandling.csv_to_dict(file_name, fieldnames, cat_info[i].get_all_cats_information())
    elapsed_time = time.time() - start_time
    tqdm.write(f"CSV {i + 1}/{len(cat_info)} 出力完了 (所要時間: {elapsed_time:.2f}秒)")