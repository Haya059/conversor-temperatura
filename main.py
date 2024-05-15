qual_unidade = input('Você deseja converter para F ou para K? ')


def c_para_f():
    temp_f = float((temp_inserida * 1.8) + 32)
    print(f'{temp_inserida}C é {temp_f}F')

def c_para_k():
    temp_k = float(temp_inserida + 273.15)
    print(f'{temp_inserida}C é {temp_k}K')

if qual_unidade == 'F':
    temp_inserida = float(input('Digite a temperatura, em Célcius, que deseja converter: '))
    c_para_f()
elif qual_unidade == 'K':
    temp_inserida = float(input('Digite a temperatura, em Célcius, que deseja converter: '))
    c_para_k()
else:
    print('Unidade de medida não identificada. Tente novamente.')