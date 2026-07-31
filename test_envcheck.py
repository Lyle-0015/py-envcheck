from envcheck import missing


def test_missing():
    assert missing(["A", "B"], {"A": "x"}) == ["B"]
    assert missing(["A"], {"A": ""}) == ["A"]
