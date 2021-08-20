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
opcao_disco_grade = input("->")

if opcao_disco_grade == "00":
    exec(open("menu.py").read())

if opcao_disco_grade == "0":
    exec(open("discos.py").read())

if opcao_disco_grade == "1":
    os.system("cls")
    print("Desconto aplicado = -5% -15% -38% -???% -10,75% +5%")
    print("")
    valor1 = input("??? = ")
    desc1 = percent(valor1 + "*5%")
    posdesc1 = float(valor1) - desc1
    posdesc1str = str(posdesc1)
    desc2 = percent(posdesc1str + "*15%")
    print(desc2)
    input()

else:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar")
    exec(open("disco_grade.py").read())
    
