def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

from funcoes import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(-5, -5) == -10
