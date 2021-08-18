import os

os.system("title " + "Calculadora de Precos - Metisa")

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
    os.system("cls")
    print("Escolha qual tipo de disco...")
    print("")
    print("1 - Grade/Arado")
    print("")
    print("2 - Plantadeira/Roda Guia")
    print("")
    input("->")

else:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar ao menu principal")
    os.system("cls")
    exec(open("Menu.py").read())
    
