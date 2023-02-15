import os

os.system("cls")
print("---Laminas---")
print()
print("Escolha uma opcao")
print()
print("0 - Voltar")
print()
print("1 - Motoniveladora")
print()
print("2 - Motoniveladora AR-1")
print()
print("3 - Perfil de nivelamento")
print()
opcao_lamina = input("->")

if opcao_lamina == "0":
    exec(open("menu.py").read())

if opcao_lamina == "1":
    exec(open("laminas/laminas_moto.py").read())

if opcao_lamina == "2":
    exec(open("laminas/laminas_moto_ar1.py").read())

if opcao_lamina == "3":
    exec(open("laminas/laminas_perfil.py").read())

if opcao_lamina not in {"0", "1", "2", "3"}:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print()
    input("Pressione enter para voltar")
    exec(open("laminas/laminas.py").read())
