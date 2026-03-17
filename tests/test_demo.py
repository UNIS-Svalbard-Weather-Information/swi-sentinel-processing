from src.demo import demo_fct


def test_demo(capsys):
    assert demo_fct(5) == 5
    assert demo_fct(4) == 3
    assert demo_fct(6) == 5
