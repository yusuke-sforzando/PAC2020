
from math import isclose
import random


from main import main
from main import parse_args
import sys

# Charactorsの定義
charactors = ["ドラえもん", "ドラミ", "野比のび太", "源静香", "骨川スネ夫"]

# ランダムの中央値と許容誤差の定義
random_center = 1 / 3
absolute_tolerance: float = 1 / 10


# 一人目が静香のときのテスト
def test_first_Sizuka():
    result = main("源静香", random.choice(charactors), 1000)
    assert isclose(random_center, result[0]
                   [0], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [2], abs_tol=absolute_tolerance)


# 二人目が静香のときのテスト
def test_second_Sizuka():
    result = main("野比のび太", "源静香", 1000)
    assert isclose(random_center, result[1]
                   [0], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [2], abs_tol=absolute_tolerance)


# 両方が静香のときのテスト
def test_two_Sizuka():
    result = main("源静香", "源静香", 1000)
    assert isclose(random_center, result[0]
                   [0], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [2], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [0], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [2], abs_tol=absolute_tolerance)


# ドラえもんのテスト
def test_Doraemon():
    result = main("ドラえもん", "野比のび太", 1000)
    assert result[0][0] == 1.0


# ドラミのテスト
def test_Dorami():
    result = main("ドラミ", "野比のび太", 1000)
    random_center: float = 1 / 2
    random_quarter: float = 1 / 4
    assert isclose(random_center, result[0]
                   [0], abs_tol=absolute_tolerance)
    assert isclose(random_quarter, result[0]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_quarter, result[0]
                   [2], abs_tol=absolute_tolerance)


# スネ夫のテスト
def test_Suneo():
    result = main("骨川スネ夫", "野比のび太", 1000)
    random_center: float = 1 / 2
    assert result[0][0] == 0.0
    assert isclose(random_center, result[0]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [2], abs_tol=absolute_tolerance)


def test_arg():
    parser = parse_args(sys.argv[1:])
    print(parser)
