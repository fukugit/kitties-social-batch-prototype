import os
import csv


class CsvHandling:

    # csvファイル名を取得，血統書のファイル名と同じにする
    @staticmethod
    def get_csv_file_name(image_path):
        return os.path.splitext(image_path)[0] + ".csv"

    # csvを出力
    @staticmethod
    def csv_to_dict(csv_file_name, required_field, data):
        if not os.path.exists("./csv_output"):
            os.mkdir("./csv_output")
        writer = csv.DictWriter(
            open(
                "./csv_output/" + csv_file_name,
                "w", newline=''),
            fieldnames=required_field)

        writer.writeheader()
        for i in data:
            writer.writerow(i.__dict__)