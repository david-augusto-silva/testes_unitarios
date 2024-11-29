def reverse(num: int):
    if(num < 0 ):
        print("Número inválido. Digite um poitivo")
        return None
    invertido = 0
    while num !=0:
        digito = num %10
        invertido = invertido*10 + digito
        num //= 10
    return invertido

def reverse2(num):
    test = str(num)
    if test.isnumeric():
        if(num < 0):
            #print("Número inválido. Digite um número positivo")
            return None
    else:
        #print("Entrada inválida. Insira apenas números")
        return None

    num_s = str(num)
    num_l = list(num_s)
    num_l.reverse()
    inverted = ''.join(num_l)
    return int(inverted)

print(type("123"))