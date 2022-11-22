
import string


def leiaDinheiro():
    def error(i):
        print(f'\033[31mERRO! "{i}" não é um valor válido, por favor, tente novamente\033[0;0m')
        leiaDinheiro()

    def stringCommaDivider(i):
        print(i)
        i[10] = "C"
        print(i)
        pass
    

    i = input()
    
    stringCommaDivider(i)


    if i.isnumeric():
        i = float(i)
    elif not i.isalnum():
        if ',' in i:
            i = float(i.replace(',','.'))
        elif '.' in i:
            i = float(i)
        else:
            error(i)
    else:
        error(i)
    return i




leiaDinheiro()

















