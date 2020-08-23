from main import main
import random

character = ["源静香", "野比のび太", "ドラえもん", "骨川スネ夫", "ドラミ"]
# ランダムの中央値と許容誤差の定義
random_center = float(1/3)
allowable_error = float(1/10)
min = random_center - allowable_error
max = random_center + allowable_error

def test_first_Sizuka():
    result = main("源静香", "野比のび太", 100)
    assert min < result[0] < max
    assert min < result[1] < max
    assert min < result[2] < max

def test_second_Sizuka():
    result = main("野比のび太","源静香", 1000)
    assert min < result[0] < max
    assert min < result[1] < max
    assert min < result[2] < max

def test_two_Sizuka():
    result = main("源静香","源静香", 1000)
    assert min < result[0] < max
    assert min < result[1] < max
    assert min < result[2] < max

def test_another_one():
    result = main("渡邉裕介",random.choice(character),1000)
    assert 
