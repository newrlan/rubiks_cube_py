import pytest
from pathlib import Path
import os

from rubik.group import Rubik
from rubik.coloring import Vector
from rubik.permutation import RubikSmallGroup


def test_Rubik_read():
    abs_path = os.path.dirname(__file__)
    file = os.path.join(abs_path, 'state_300423.txt')
    file = Path(file)
    state = Rubik.load(file)
    assert state.coloring[Vector(1, 1, 1)] == Vector(-1, 1, 1)


def test_Rubik_apply_word():
    abs_path = os.path.dirname(__file__)
    file = os.path.join(abs_path, 'state_300423.txt')
    file = Path(file)
    cube = Rubik.load(file)

    p = cube.permutation(subgroup='vertex')
    word = RubikSmallGroup().permutation2word(p)

    cube.apply(word)
    q = cube.permutation(subgroup='vertex')
    assert q.len() == 0
