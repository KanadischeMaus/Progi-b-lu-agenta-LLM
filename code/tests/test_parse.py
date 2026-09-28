from agent.parse import parse_action, strip_thinking


def test_poprawne():
    assert parse_action("2") == (2, "ok")
    assert parse_action("<think>bateria niska, 1 albo 2</think>\n2") == (2, "ok")
    assert parse_action("**Answer: 0**") == (0, "ok")          # listing 15
    assert parse_action("Action: 7") == (7, "ok")


def test_bledne():
    assert parse_action("") == (None, "pusta")
    assert parse_action("<think>...</think>") == (None, "pusta")
    assert parse_action("I choose to water") == (None, "brak_liczby")
    assert parse_action("0-7") == (None, "wiele_liczb")
    assert parse_action("2 (not 1)") == (None, "wiele_liczb")
    assert parse_action("9") == (None, "poza_zakresem")
    assert parse_action("12") == (None, "brak_liczby")         # \b\d\b nie łapie liczb wielocyfrowych


def test_samo_zamkniecie_think():
    ans, th = strip_thinking("rozumowanie bez otwarcia</think>\n\n4")
    assert ans == "4" and "rozumowanie" in th
    assert parse_action("rozumowanie 1 2 3</think>4") == (4, "ok")
