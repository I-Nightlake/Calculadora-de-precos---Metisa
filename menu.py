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
    
# Início do código do arquivo discos.py
    
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
    exec(open("disco_grade").read())

if opcao_disco == "2":
    exec(open("disco_plantadeira").read())

else:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar")
    exec(open("discos.py").read())

# Fim do código do arquivo discos.py

if opcao == "2":
    exec(open("laminas.py").read())
    
# Início do código do arquivo laminas.py

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
    exec(open("lamina_moto").read())

if opcao_lamina == "2":
    exec(open("lamina_perfil").read())
    
# Fim do código do arquivo laminas.py

else:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar")
    exec(open("laminas.py").read())

else:
    os.system("cls")
    print("Comando invalido, tente novamente...")
    print("")
    input("Pressione enter para voltar")
    exec(open("menu.py").read())
    
