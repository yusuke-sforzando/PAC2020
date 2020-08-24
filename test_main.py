from main import main

# ランダムの中央値と許容誤差の定義
random_center = float(1 / 3)
allowable_error = float(1 / 10)
min = random_center - allowable_error
max = random_center + allowable_error


def test_first_Sizuka():
    result = main("源静香", "野比のび太", 1000)
    assert min < result[0] < max
    assert min < result[1] < max
    assert min < result[2] < max


def test_second_Sizuka():
    result = main("野比のび太", "源静香", 1000)
    assert min < result[0] < max
    assert min < result[1] < max
    assert min < result[2] < max


def test_two_Sizuka():
    result = main("源静香", "源静香", 1000)
    assert min < result[0] < max
    assert min < result[1] < max
    assert min < result[2] < max
