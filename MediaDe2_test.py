import pytest
from MediaDe2 import MediaDe2

def test_calcular_media(): 
    numero1 = 4
    numero2 = 6
    
    assert calcular_media(numero1, numero2) == 5.0

def test_calcular_media_tipos_invalidos():
    with pytest.raises(TypeError):
        calcular_media("4", 6)
