import pytest
from media2TDD import media2TDD 

def test_calcular_media():
    assert calcular_media(4, 6) == 5.0

    assert calcular_media(4.5, 6.5) == 5.5

    assert calcular_media(4, 6.5) == 5.25

    assert calcular_media(0, 5) == 2.5

    with pytest.raises(TypeError):
        calcular_media("4", 6)
