from main import main

import random


# Charactorsの定義
charactors = ["ドラえもん", "ドラミ", "野比のび太", "源静香", "骨川スネ夫"]
# ランダムの中央値と許容誤差の定義
random_center = 1 / 3
allowable_error = 1 / 10
min = random_center - allowable_error
max = random_center + allowable_error

# 一人目が静香のときのテスト


def test_first_Sizuka():
    result = main("源静香", random.choice(charactors), 1000)
    assert min < result[0][0] < max
    assert min < result[0][1] < max
    assert min < result[0][2] < max

# 二人目が静香のときのテスト


def test_second_Sizuka():
    result = main("野比のび太", "源静香", 1000)
    assert min < result[1][0] < max
    assert min < result[1][1] < max
    assert min < result[1][2] < max

# 両方が静香のときのテスト


def test_two_Sizuka():
    result = main("源静香", "源静香", 1000)
    assert min < result[0][0] < max
    assert min < result[0][1] < max
    assert min < result[0][2] < max
    assert min < result[1][0] < max
    assert min < result[1][1] < max
    assert min < result[1][2] < max

# ドラえもんのテスト


def test_Doraemon():
    result = main("ドラえもん", "野比のび太", 1000)
    assert result[0][0] == 1

# ドラミのテスト


def test_Dorami():
    result = main("ドラミ", "野比のび太", 1000)
    random_center = 1 / 2
    allowable_error = 1 / 10
    min = random_center - allowable_error
    max = random_center + allowable_error
    assert min < result[0][0] < max
    assert min / 2 < result[0][1] < max / 2
    assert min / 2 < result[0][2] < max / 2


def test_Suneo():
    result = main("骨川スネ夫", "野比のび太", 1000)
    random_center = 1 / 2
    allowable_error = 1 / 10
    min = random_center - allowable_error
    max = random_center + allowable_error
    assert result[0][0] == 0
    assert min < result[0][1] < max
    assert min < result[0][2] < max
