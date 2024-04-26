import pytest
from media2TDD import calcular_media

def test_calcular_media():
    # Teste para verificar se a função retorna a média correta de dois números inteiros
    assert calcular_media(4, 6) == 5.0

    # Teste para verificar se a função retorna a média correta de dois números decimais
    assert calcular_media(4.5, 6.5) == 5.5

    # Teste para verificar se a função retorna a média correta de um número inteiro e um número decimal
    assert calcular_media(4, 6.5) == 5.25

    # Teste para verificar se a função retorna a média correta quando um dos números é zero
    assert calcular_media(0, 5) == 2.5

    # Teste para verificar se a função lança uma exceção quando um dos argumentos não é um número
    with pytest.raises(TypeError):
        calcular_media("4", 6)
