from __future__ import annotations
from pathlib import Path
from os import chdir
import pydantic
import yaml
from dataclasses import dataclass



def main() -> None:
    # print(f'Current dir: {Path.cwd()}.')
    # print(f'Home dir: {Path.home()}.')

    # path = Path('/mnt/c/python')
    # path1 = Path('/mnt') / 'c' / 'python'
    # # check if path exists
    # print(path.exists())
    # print(path1.exists())

    home_path = Path.cwd() / 'data_file.json'
    with home_path.open() as file:
        print(file.read())
    # # # same as
    # print(home_path.read_text())


    path = Path('data_file.json')
    print(path.resolve())
    # >>> /mnt/c/python/repos2_orig/repos2/python/data_file.json   Absolute path

    full_path = path.resolve()
    print(full_path.parent)
    # >>> /mnt/c/python/repos2_orig/repos2/python  parent folder
    print(full_path.name)
    # data_file.json
    print(full_path.is_dir())
    print(full_path.is_file())
    print(full_path.suffix)
    # False
    # True
    # .json


    # create new file
    new_file = Path.cwd() / 'new_file.txt'
    new_file.touch()
    # writing text to new file
    new_file.write_text('this text')
    # deleting the file
    new_file.unlink()

    # creating new directory
    new_dir = Path.cwd() / 'new_dir'
    # new_dir.mkdir()

    # changing cwd(current workig directory) | os.chdir
    # chdir(new_dir)
    # print(f'Current working directory: {Path.cwd()}')
    # deleting the directory
    new_dir.rmdir()



# if __name__ == '__main__':
#     main()



# Pathlib working with dataclasses | doesnt work !
class PydanticSettings(pydantic.BaseModel):
    path: Path
    other: str


@dataclass
class Settings:
    path: Path
    other: str


def path_class():
    path = Path.cwd() / 'yaml_example.yml'
    parsed_yaml = yaml.safe_load(path.read_text())
    settings = Settings(**parsed_yaml) # wont work
    # settings = PydanticSettings(**parsed_yaml)
    print(settings)
    print(settings.path.parent)

# path_class()



# dunder method for operators
@dataclass
class Vector:
    x: float
    y: float

    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other)
    
    def __add__(self, other: Vector) -> Vector:
        return (self.x + other.x, self.y + other.y)


def main_points():
    point = Vector(1, 2)
    print(point + point / 2)


if __name__ == '__main__':
        main_points()
















