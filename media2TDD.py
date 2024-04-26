def calcular_media(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError("Os números devem ser inteiros ou floats")
    
    return (num1 + num2) / 2
