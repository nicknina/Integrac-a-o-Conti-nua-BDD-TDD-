import pytest

def test_calcular_media():
    # Cenário: Calcular a média de dois números
    numero1 = 4
    numero2 = 6
    
    # Verificar se a função retorna a média correta
    assert calcular_media(numero1, numero2) == 5.0

def test_calcular_media_tipos_invalidos():
    # Cenário: Lidar com tipos de dados inválidos
    with pytest.raises(TypeError):
        calcular_media("4", 6)
def calcular_media(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError("Os números devem ser inteiros ou floats")
    
    return (num1 + num2) / 2
