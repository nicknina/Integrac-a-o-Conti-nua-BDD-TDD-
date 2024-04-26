import pytest
from MediaDe2 import calcular_media

def test_calcular_media(): 
    numero1 = 4
    numero2 = 6
    
    # Verificar se a função retorna a média correta
    assert calcular_media(numero1, numero2) == 5.0

def test_calcular_media_tipos_invalidos():
    with pytest.raises(TypeError):
        calcular_media("4", 6)
