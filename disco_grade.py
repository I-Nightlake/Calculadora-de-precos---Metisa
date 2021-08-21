import os


def percent(expression):
    if "%" in expression:
        expression = expression.replace("%", "/100")
    return eval(expression)


os.system("cls")
print("---Discos de Grade/Arado---")
print("")
print("Escolha uma opcao")
print("")
print("00 - Menu Principal")
print("")
print("0 - Voltar")
print("")
print('1 - Ate 20" e 28"')
print("")
print('2 - 22"')
print("")
print('3 - 24" e 26"')
print("")
print('4 - 30" para cima')
print("")
opcao_disco_grade = input("->")

if opcao_disco_grade == "00":
    exec(open("menu.py").read())

if opcao_disco_grade == "0":
    exec(open("discos.py").read())

if opcao_disco_grade == "1":
    os.system("cls")
    print("Desconto aplicado = -5% -15% -38% -???% -10,75% +5%")
    print("")

while True:
    try:
        valor_desconto = str(input("4° Desconto ->"))
        if ('a' <= valor_desconto <= 'z') or ('A' <= valor_desconto <= 'Z'):
            raise ValueError("O desconto precisa ser um número...")
    except ValueError as ve1:
        print(ve1)
    else:
        break

print("")

while True:
    try:
        valor1 = input("Valor do item->")
        if ('a' <= valor1 <= 'z') or ('A' <= valor1 <= 'Z'):
            raise ValueError("O valor do item precisam ser um número...")
    except ValueError as ve2:
        print(ve2)
    else:
        break

desc1 = percent(valor1 + "*5%")
posdesc1 = float(valor1) - desc1
posdesc1str = str(posdesc1)
desc2 = percent(posdesc1str + "*15%")
posdesc2 = posdesc1 - desc2
posdesc2str = str(posdesc2)
desc3 = percent(posdesc2str + "*38%")
posdesc3 = posdesc2 - desc3
posdesc3str = str(posdesc3)
desc4 = percent(posdesc3str + "*" + valor_desconto + "%")
posdesc4 = posdesc3 - desc4
posdesc4str = str(posdesc4)
desc5 = percent(posdesc4str + "*10.75%")
posdesc5 = posdesc4 - desc5
posdesc5str = str(posdesc5)
ipi = percent(posdesc5str + "*5%")
posipi = posdesc5 + ipi
posipistr = str(posipi)
print("")
print("À Vista? (3% de Desconto)")
print("")
print("1 - Sim")
print("")
print("2 - Não")
print("")

while True:
    try:
        avista1 = input("->")
        if avista1 == "1":
            break
        if avista1 == "2":
            break
        else:
            raise ValueError("Opcao invalida")
    except ValueError as ve3:
        print(ve3)

if avista1 == "1":
    valor_avista = percent(posipistr + "*3%")
    posvalor_avista = posipi - valor_avista
    posvalor_avistastr = str(posvalor_avista)
    print("")
    print("Valor Unitário Final: R$ " + posvalor_avistastr)

if avista1 == "2":
    print("")
    print("Valor Unitário Final: R$ " + posipistr)
    print("")

input("Pressione enter para voltar...")
exec(open("disco_grade.py").read())
    
