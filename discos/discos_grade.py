import os

os.system("cls")

print("---Discos de Grade/Arado---")
print()
print("Escolha uma opcao")
print()
print("00 - Menu Principal")
print()
print("0 - Voltar")
print()
print('1 - Ate 20" e 28"')
print()
print('2 - 22"')
print()
print('3 - 24" e 26"')
print()
print('4 - 30" para cima')
print()
opcao_disco_grade = input("->")

if opcao_disco_grade == "00":
    exec(open("menu.py").read())

if opcao_disco_grade == "0":
    exec(open("discos/discos.py").read())

if opcao_disco_grade == "1":
    exec(open("discos/discos_grade_20_28.py").read())

if opcao_disco_grade == "2":
    exec(open("discos/discos_grade_22.py").read())

if opcao_disco_grade == "3":
    exec(open("discos/discos_grade_24_26.py").read())

if opcao_disco_grade == "4":
    exec(open("discos/discos_grade_30.py").read())

if opcao_disco_grade not in {"00", "0", "1", "2", "3", "4"}:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print()
    input("Pressione enter para voltar")
    exec(open("discos/discos_grade.py").read())
