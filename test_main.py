
from math import isclose
import pytest
import random

from hand import Janken_Hand
from main import main
from main import Player

# Charactorsの定義
charactors = ["ドラえもん", "ドラミ", "野比のび太", "源静香", "骨川スネ夫"]

# ランダムの中央値と許容誤差の定義
random_center = 1 / 3
absolute_tolerance: float = 1 / 10


# 予期しない入力値を判定できるかのテスト
def test_catch():
    with pytest.raises(ValueError) as ve:
        main("渡邉裕介", "広瀬すず", 100)
    assert "There is no such person" in str(ve)
    with pytest.raises(ValueError) as ve:
        main("源静香", "野比のび太", 10001)
    assert "Out of range" in str(ve)


# Class Player neme()のテスト
def test_name():
    charactor = random.choice(charactors)
    test_player = Player(charactor).name
    assert test_player == "Player" + charactor


# 一人目が静香のときのテスト
def test_first_Sizuka():
    result = main("源静香", random.choice(charactors), 500)
    assert isclose(random_center, result[0]
                   [0], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [2], abs_tol=absolute_tolerance)


# 二人目が静香のときのテスト
def test_second_Sizuka():
    result = main("野比のび太", "源静香", 500)
    assert isclose(random_center, result[1]
                   [0], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [2], abs_tol=absolute_tolerance)


# 両方が静香のときのテスト
def test_two_Sizuka():
    result = main("源静香", "源静香", 500)
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
    result = main("ドラえもん", "野比のび太", 500)
    assert result[0][0] == 1.0
    result = main("野比のび太", "ドラえもん", 500)
    assert result[1][0] == 1.0


# ドラミのテスト
def test_Dorami():
    result = main("ドラミ", "ドラミ", 500)
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
    result = main("骨川スネ夫", "骨川スネ夫", 500)
    random_center: float = 1 / 2
    assert result[0][0] == 0.0
    assert result[1][0] == 0.0
    assert isclose(random_center, result[0]
                   [1], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[0]
                   [2], abs_tol=absolute_tolerance)
    assert isclose(random_center, result[1]
                   [2], abs_tol=absolute_tolerance)


# ジャンケンのテスト
def test_janken():
    goo = Janken_Hand(0)
    chii = Janken_Hand(1)
    paa = Janken_Hand(2)
    assert str(goo) == "グー"
    assert str(chii) == "チョキ"
    assert str(paa) == "パー"


if __name__ == "__main__":
    test_name()
