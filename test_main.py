
from math import isclose
import random

from hand import Janken_Hand
from main import main
from main import Player
from strategy import Doraemon_Strategy
from strategy import Dorami_Strategy
from strategy import Janken_Strategy
from strategy import Nobita_Strategy
from strategy import Sizuka_Strategy
from strategy import Suneo_Strategy


# Charactorsの定義
charactors = ["ドラえもん", "ドラミ", "野比のび太", "源静香", "骨川スネ夫"]

# ランダムの中央値と許容誤差の定義
random_center = 1 / 3
absolute_tolerance: float = 1 / 10


def test_arg():
    # parser = parse_args(sys.argv[1:])
    # assert parser.first in ["源静香", "野比のび太", "ドラえもん", "骨川スネ夫", "ドラミ"]
    # assert parser.second in ["源静香", "野比のび太", "ドラえもん", "骨川スネ夫", "ドラミ"]
    # assert 0 < parser.trials < 1000
    pass


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


# ジャンケンのテスト
def test_janken():
    goo = Janken_Hand(0)
    chii = Janken_Hand(1)
    paa = Janken_Hand(2)
    assert str(goo) == "グー"
    assert str(chii) == "チョキ"
    assert str(paa) == "パー"


def test_win_lose():
    player1 = Player(random.choice(charactors))
    player2 = Player(random.choice(charactors))
    assert player1.next_hand().value == 1
    assert player2.next_hand().value == 1
    player1.strategy = Doraemon_Strategy()
    player2.strategy = Dorami_Strategy()
    hand1 = player1.next_hand().value
    hand2 = player2.next_hand().value
    assert hand1 in [0, 1, 2]
    assert hand2 in [0, 1, 2]

    player1.strategy = Suneo_Strategy()
    player2.strategy = Sizuka_Strategy()
    hand1 = player1.next_hand().value
    hand2 = player2.next_hand().value
    assert hand1 in [0, 1, 2]
    assert hand2 in [0, 1, 2]

    player1.strategy = Nobita_Strategy()
    player2.strategy = Janken_Strategy()
    hand1 = player1.next_hand().value
    hand2 = player2.next_hand().value
    assert hand1 in [0, 1, 2]
    assert hand2 in [0, 1, 2]


# ジャンケンがルール通りになっているかチェック
def judge():
    # assert hand1 in ["グー", "チョキ", "パー"]
    # あいこのとき正しいかチェック
    hand1 = Janken_Hand.goo
    hand2 = Janken_Hand.goo
    judge = True
    if hand1.win_to(hand2) or hand1.lose_to(hand2):
        judge = False
    assert judge

    hand1 = Janken_Hand.chii
    hand2 = Janken_Hand.chii
    judge = True
    if hand1.win_to(hand2) or hand1.lose_to(hand2):
        judge = False
    assert judge

    hand1 = Janken_Hand.paa
    hand2 = Janken_Hand.paa
    judge = True
    if hand1.win_to(hand2) or hand1.lose_to(hand2):
        judge = False
    assert judge


if __name__ == "__main__":
    test_win_lose()
