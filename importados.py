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

print("---Importados---")
print()
print("Desconto aplicado = -28% -5,70% +5%")
print()
print("00 - Voltar")
print()

while True:
    try:
        valor = input("Valor do item->")
        if ("a" <= valor <= "z") or ("A" <= valor <= "Z") or valor == "":
            raise ValueError("Valor invalido, tente novamente...")
        if valor == "00":
            exec(open("menu.py").read())
    except ValueError as ve1:
        print(ve1)
    else:
        break

valor_format = str(comma_to_point(valor))

desc1 = percent(valor_format + "*28%")
posdesc1 = float(valor_format) - desc1
posdesc1str = str(posdesc1)
desc2 = percent(posdesc1str + "*0%")
posdesc2 = posdesc1 - desc2
posdesc2str = str(posdesc2)
desc3 = percent(posdesc2str + "*0%")
posdesc3 = posdesc2 - desc3
posdesc3str = str(posdesc3)
desc4 = percent(posdesc3str + "*0%")
posdesc4 = posdesc3 - desc4
posdesc4str = str(posdesc4)
desc5 = percent(posdesc4str + "*5.70%")
posdesc5 = posdesc4 - desc5
posdesc5str = str(posdesc5)
ipi = percent(posdesc5str + "*5%")
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
            exec(open("importados.py").read())
        if avista == "1" or avista == "2":
            break
        else:
            raise ValueError("Opcao invalida, tente novamente...")
    except ValueError as ve2:
        print(ve2)

if avista == "1":
    print()
    print("Valor Unitario Final: R$ " + posipistr)
    print()
    input("Pressione enter para voltar")
    exec(open("importados.py").read())

if avista == "2":
    valor_avista = percent(posipistr + "*3%")
    posvalor_avista = posipi + valor_avista
    posvalor_avistastr = str(posvalor_avista)
    print()
    print("Valor Unitario Final: R$ " + posvalor_avistastr)
    print()
    input("Pressione enter para voltar")
    exec(open("importados.py").read())
