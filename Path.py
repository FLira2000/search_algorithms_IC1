from enum import Enum


class Directions(Enum):
    DOWN = 1
    LEFT = 2
    UP = 3
    RIGHT = 4


class Path:
    _down = None
    _left = None
    _up = None
    _right = None

    def __init__(self, letter):
        self.letter = letter

    def add_path(self, direction, new_path_letter):
        if direction == Directions.DOWN and self._down is None:
            self._down = Path(new_path_letter)
        elif direction == Directions.LEFT and self._left is None:
            self._left = Path(new_path_letter)
        elif direction == Directions.UP and self._up is None:
            self._up = Path(new_path_letter)
        elif direction == Directions.RIGHT and self._right is None:
            self._right = Path(new_path_letter)

    def to_iter(self):
        path_dict = {}
        path_dict = {**path_dict, 'down': self._down} if self._down is not None else path_dict
        path_dict = {**path_dict, 'left': self._left} if self._left is not None else path_dict
        path_dict = {**path_dict, 'up': self._up} if self._up is not None else path_dict
        path_dict = {**path_dict, 'right': self._right} if self._right is not None else path_dict

        return path_dict.items()

    def can_have_new_path(self):
        conditions = [
            self._down is None,
            self._left is None,
            self._up is None,
            self._right is None
        ]

        return any(conditions)
