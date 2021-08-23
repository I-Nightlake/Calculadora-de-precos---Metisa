import os

os.system("cls")
print("---Laminas---")
print("")
print("Escolha uma opcao")
print("")
print("0 - Voltar")
print("")
print("1 - Motoniveladora")
print("")
print("2 - Perfil de nivelamento")
print("")
opcao_lamina = input("->")

if opcao_lamina == "0":
    exec(open("menu.py").read())

if opcao_lamina == "1":
    exec(open("lamina_moto.py").read())

if opcao_lamina == "2":
    exec(open("lamina_perfil.py").read())

else:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar")
    exec(open("laminas.py").read())
