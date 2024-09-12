def analizar_palabra(palabra):
    """
    Analiza la palabra y muestra los numeros romanos encontrados con sus valores.

    Args:
        Palabra: palabra a analizar
    """

    valores_rom = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
    valor_total = 0
    num_rom = []

    for letra in palabra:
        if letra in valores_rom:
            valor_actual = valores_rom[letra]
            num_rom.append((letra,valor_actual))
            valor_total += valor_actual
    print(f"Palabra: {palabra}")
    if num_rom:
        print("Numeros encontrados: ")
        for letra, valor in num_rom:
            print(f"-{letra}: {valor}")
    else:
        print("No se encontraron numeros romanos en la palabra")