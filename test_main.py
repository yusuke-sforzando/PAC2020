from main import main


def test_main():
    result = main("源静香", "野比のび太", 1000)
    assert result[0] < 0.4
    assert result[1] < 0.4
    assert result[2] < 0.4
