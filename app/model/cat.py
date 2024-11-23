from pydantic import BaseModel
from typing import List

class Cat(BaseModel):
    no: int
    name: str
    breed: str
    sex: str
    eye_color: str
    color: str
    date_of_birth: str
    registration_number: str
    breeder: str
    owner: str
    date_of_registration: str


class Cats(BaseModel):
    cats: List[Cat]

    def get_all_cats_information(self):
        return self.cats