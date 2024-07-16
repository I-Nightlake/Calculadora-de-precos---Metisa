import os

os.system("title " + "Calculadora de Precos - Metisa - 1.4.1")
os.system("cls")

print("---Menu Principal---")
print()
print("Escolha uma opcao")
print()
print("0 - Sair")
print()
print("1 - Discos")
print()
print("2 - Laminas")
print()
print("3 - Dentes")
print()
print("4 - Importados")
print()
print("5 - Implementos Agricolas")
print()
print("6 - Creditos")
print()
opcao = input("->")

if opcao == "0":
    exit()

if opcao == "1":
    exec(open("discos/discos.py").read())

if opcao == "2":

    exec(open("laminas/laminas.py").read())

if opcao == "3":
    exec(open("dentes/dentes.py").read())

if opcao == "4":
    exec(open("importados/importados.py").read())

if opcao == "5":
    exec(open("implementos-agricolas/implementos_agricolas.py").read())

if opcao == "6":
    os.system("cls")
    print("Calculadora de precos - Metisa- 1.4.1")
    print()
    print("Criada e idealizada por Italo Miguel Souza")
    print()
    print()
    input("Pressione enter para voltar ao menu")
    exec(open("menu.py").read())

if opcao not in {"0", "1", "2", "3", "4", "5", "6"}:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print()
    input("Pressione enter para voltar")
    exec(open("menu.py").read())
