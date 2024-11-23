from image_handling import ImageHandling

# 団体のpromptを作成
class BasePrompt:

    # system promptでopenaiの役割を指定
    @staticmethod
    def get_identification_prompt():
        return """
        A CERTIFIED PEDIGREE is a picture of a cat's pedigree.
        You are a super assistant who are good at checking CERTIFIED PEDIGREE for cats and getting information from CERTIFIED PEDIGREE.
        You only answer with the information I asked for. You also only get the answer from the picture of CERTIFIED PEDIGREE and never try to create answer which is not in the picture.
        If you cannot find the information I asked for, you always reply me by an empty string like '' or 'None'.
        """

    # 血統書に乗っている猫自身の情報を指定
    @staticmethod
    def get_cat_self_prompt():
        return """
        A CERTIFIED PEDIGREE always includes the information for name, breed, sex, eye color, color, date of birth, registration number, breeder, owner and date of registration of the cat.
        The second line in the right column shows the date of registration and the third line shows the date of birth
        The information of the cat is always written in the top of the CERTIFIED PEDIGREE.
        Let's say this cat is cat No.0.
        """

    # 血統書に乗っている猫の家族の情報を指定
    @staticmethod
    def get_cat_relatives_prompt():
        return """
        Also, a CERTIFIED PEDIGREE always includes the name, color, eye color, and registration number of the cat's relatives.
        The cat's relatives refers to the cat's parents, grandparents and great grandparents(at least fourteen cats).
        The relationship between the cat and the cat's relatives is always shown in trees structures.
        There are two trees in the picture, one is the tree is for of the cat's SIRE and the other is for the cat's DAM.
        Both of the trees located under the information of the cat.
        There are always numbers in the information of the cat's relatives which can make you identify easily.
        Cat No.1 is the cat's SIRE and cat No.2 is the cat's DAM.
        Cat No.1's parents are cat No.3(SIRE) and No.4(DAM).
        Cat No.2's parents are cat No.5(SIRE) and No.6(DAM).
        Cat No.3's parents are cat No.7(SIRE) and No.8(DAM).
        Cat No.4's parents are cat No.9(SIRE) and No.10(DAM).
        Cat No.5's parents are cat No.11(SIRE) and No.12(DAM).
        Cat No.6's parents are cat No.13(SIRE) and No.14(DAM).
        Cats' names are near to each other and always on the right side of the number, so be careful not to misread.
        Information for cat No.1 to No.14 are written in four lines, the first line is the name, the second line is the color, the third line is the eye color and the fourth line is the registration number.
        Some of the CERTIFIED PEDIGREEEs are written in English while others are written in Japanese and English.
        """

    # openaiの役割+猫情報+猫の家族情報でシステムpromptを作成
    @staticmethod
    def create_system_prompt():
        return {"role": "system", "content": BasePrompt.get_identification_prompt() + BasePrompt.get_cat_self_prompt() + BasePrompt.get_cat_relatives_prompt()}

    # 血統書の画像を読み込んでbase64にエンコードし，user promptを作成
    @staticmethod
    def get_image_upload_prompt(image):
        return [
            {
                "type": "text",
                "text": """I will show you a CERTIFIED PEDIGREE for a cat
                               """,
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{ImageHandling.encode_image(ImageHandling.get_specify_image_path(image))}",
                    "detail":"high"
                }
            }
        ]

    # 問題のuser promptを作成
    @staticmethod
    def get_required_information():
        return """please tell me:
                1.name, breed, sex, eye color, color, date of birth, registration number, breeder, owner and date of registration of this cat which is cat No.0.
                2.name, color, eye color and registration number for cat No.1 to No.14.
                               """

    # user promptを作成
    @staticmethod
    def create_user_prompt(image):
        image_prompt = {"role": "user",
                        "content": BasePrompt.get_image_upload_prompt(image)}
        required_information_prompt = {"role": "user",
                                       "content": BasePrompt.get_required_information()}
        return [image_prompt, required_information_prompt]

