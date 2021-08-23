import os

os.system("cls")
print("---Discos---")
print("")
print("Escolha uma opcao")
print("")
print("0 - Voltar")
print("")
print("1 - Grade/Arado")
print("")
print("2 - Plantadeira/Roda Guia")
print("")
opcao_disco = input("->")

if opcao_disco == "0":
    exec(open("menu.py").read())

if opcao_disco == "1":
    exec(open("disco_grade.py").read())

if opcao_disco == "2":
    exec(open("disco_plantadeira.py").read())

else:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar")
    exec(open("discos.py").read())
