import os


def percent(expression):
    if "%" in expression:
        expression = expression.replace("%", "/100")
    return eval(expression)


def comma_to_point(expression):
    if "," in expression:
        expression = expression.replace(",", ".")
    return eval(expression)


os.system("cls")

print("---Laminas Perfil---")
print()
print("Desconto aplicado = -5% -15% -13,50% -##% -10,75% +3,75%")
print()
print("00 - Voltar")
print()

while True:
    try:
        desconto = input("Desconto ## ->")
        if ("a" <= desconto <= "z") or ("A" <= desconto <= "Z") or desconto == "":
            raise ValueError("Desconto invalido, tente novamente...")
        if "00000001" <= desconto <= "09999999":
            raise ValueError("Numeros nao podem comecar com 0, sendo este um numero inteiro")
    except ValueError as ve1:
        print()
        print(ve1)
        print()
    else:
        break

if desconto == "00":
    exec(open("laminas.py").read())

desconto_format = str(comma_to_point(desconto))

print()

while True:
    try:
        valor = input("Valor do item->")
        if ("a" <= valor <= "z") or ("A" <= valor <= "Z") or valor == "":
            raise ValueError("Valor invalido, tente novamente...")
        if "00000001" <= valor <= "09999999":
            raise ValueError("Numeros nao podem comecar com 0, sendo este um numero inteiro")
        if valor == "00":
            exec(open("laminas_perfil.py").read())
    except ValueError as ve2:
        print(ve2)
    else:
        break

valor_format = str(comma_to_point(valor))

desc1 = percent(valor_format + "*5%")
posdesc1 = float(valor_format) - desc1
posdesc1str = str(posdesc1)
desc2 = percent(posdesc1str + "*15%")
posdesc2 = posdesc1 - desc2
posdesc2str = str(posdesc2)
desc3 = percent(posdesc2str + "*13.50%")
posdesc3 = posdesc2 - desc3
posdesc3str = str(posdesc3)
desc4 = percent(posdesc3str + "*" + desconto_format + "%")
posdesc4 = posdesc3 - desc4
posdesc4str = str(posdesc4)
desc5 = percent(posdesc4str + "*10.75%")
posdesc5 = posdesc4 - desc5
posdesc5str = str(posdesc5)
ipi = percent(posdesc5str + "*3.75%")
posipi = posdesc5 + ipi
posipistr = str(posipi)
print()
print("A Vista? (3% de Desconto)")
print()
print("1 - Sim")
print()
print("2 - Nao")
print()

while True:
    try:
        avista = input("->")
        if avista == "00":
            exec(open("laminas_perfil.py").read())
        if avista == "1" or avista == "2":
            break
        else:
            raise ValueError("Opcao invalida, tente novamente...")
    except ValueError as ve3:
        print(ve3)

if avista == "1":
    print()
    print("Valor Unitario Final: R$ " + posipistr)
    print()
    input("Pressione enter para voltar")
    exec(open("laminas_perfil.py").read())

if avista == "2":
    valor_avista = percent(posipistr + "*3%")
    posvalor_avista = posipi + valor_avista
    posvalor_avistastr = str(posvalor_avista)
    print()
    print("Valor Unitario Final: R$ " + posvalor_avistastr)
    print()
    input("Pressione enter para voltar")
    exec(open("laminas_perfil.py").read())
