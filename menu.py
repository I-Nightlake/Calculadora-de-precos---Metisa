import os

os.system("title " + "Calculadora de Precos - Metisa")
os.system("cls")

print("---Menu Principal---")
print("")
print("Escolha uma opcao")
print("")
print("0 - Sair")
print("")
print("1 - Discos")
print("")
print("2 - Laminas")
print("")
print("3 - Dentes")
print("")
opcao = input("->")

if opcao == "0":
    exit()

if opcao == "1":
    exec(open("discos.py").read())

if opcao == "2":
    exec(open("laminas.py").read())

if opcao == "3":
    exec(open("dentes.py").read())

if opcao not in {"0", "1", "2", "3"}:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar")
    exec(open("menu.py").read())
