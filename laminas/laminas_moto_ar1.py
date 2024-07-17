import os
import clipboard


def percent(expression):
    if "%" in expression:
        expression = expression.replace("%", "/100")
    return eval(expression)


def comma_to_point(expression):
    if "," in expression:
        expression = expression.replace(",", ".")
    return eval(expression)


os.system("cls")

print("---Laminas Moto-AR-1---")
print()
print("Desconto aplicado = -9% -20,10% -13,50% -##% -5,70% +3,25%")
print()
print("Desconto sugerido: 27%")
print()
print("00 - Voltar")
print()

while True:
    try:
        desconto = input("Desconto ## ->")
        if ("a" <= desconto <= "z") or ("A" <= desconto <= "Z") or desconto == "":
            raise ValueError("Desconto invalido, tente novamente...")
        if "00000001" <= desconto <= "09999999":
            raise ValueError("Numeros nao podem comecar com 0, sendo este um numero inteiro")
    except ValueError as ve1:
        print()
        print(ve1)
        print()
    else:
        break

if desconto == "00":
    exec(open("laminas/laminas.py").read())

desconto_format = str(comma_to_point(desconto))

print()

while True:
    try:
        valor = input("Valor do item->")
        if ("a" <= valor <= "z") or ("A" <= valor <= "Z") or valor == "":
            raise ValueError("Valor invalido, tente novamente...")
        if "00000001" <= valor <= "09999999":
            raise ValueError("Numeros nao podem comecar com 0, sendo este um numero inteiro")
        if valor == "00":
            exec(open("laminas/laminas_moto_ar1.py").read())
    except ValueError as ve2:
        print(ve2)
    else:
        break

valor_format = str(comma_to_point(valor))

desc1 = percent(valor_format + "*9%")
posdesc1 = float(valor_format) - desc1
posdesc1str = str(posdesc1)
desc2 = percent(posdesc1str + "*20.10%")
posdesc2 = posdesc1 - desc2
posdesc2str = str(posdesc2)
desc3 = percent(posdesc2str + "*13.50%")
posdesc3 = posdesc2 - desc3
posdesc3str = str(posdesc3)
desc4 = percent(posdesc3str + "*" + desconto_format + "%")
posdesc4 = posdesc3 - desc4
posdesc4str = str(posdesc4)
desc5 = percent(posdesc4str + "*5.70%")
posdesc5 = posdesc4 - desc5
posdesc5str = str(posdesc5)
semipi = posdesc5
semipiround = round(semipi, ndigits=2)
semipiroundstr = str(semipiround)
ipi = percent(posdesc5str + "*3.25%")
posipi = posdesc5 + ipi
posipiround = round(posipi, ndigits=2)
posipiroundstr = str(posipiround)
print()
print("A Vista? (3% de Desconto)")
print()
print("1 - Sim")
print()
print("2 - Nao")
print()

while True:
    try:
        avista = input("->")
        if avista == "00":
            exec(open("laminas/laminas_moto_ar1.py").read())
        if avista == "1" or avista == "2":
            break
        else:
            raise ValueError("Opcao invalida, tente novamente...")
    except ValueError as ve3:
        print(ve3)

if avista == "1":
    print()
    print("Valor Unitario: R$ " + semipiroundstr + ". (Sem IPI)")
    print("Valor Unitario: R$ " + posipiroundstr + ". (Com IPI de 3,25% incluso)")
    print()
    print("Deseja copiar o valor para colar?")
    print()
    print("1 - Sim")
    print()
    print("2 - Nao")
    print()
    while True:
        try:
            copiar = input("->")
            linha11 = ("Valor Unitario: R$ " + semipiroundstr + ". (Sem IPI)")
            linha12 = ("Valor Unitario: R$ " + posipiroundstr + ". (Com IPI de 3,25% incluso)")
            if copiar == "1":
                clipboard.copy(linha11 + "\n" + linha12)
            if copiar == "1" or copiar == "2":
                break
            else:
                raise ValueError("Opcao invalida, tente novamente...")
        except ValueError as ve3:
            print(ve3)
    print()
    input("Pressione enter para voltar")
    exec(open("laminas/laminas_moto_ar1.py").read())

if avista == "2":
    valor_avistasemipi = percent(semipiroundstr + "*3%")
    posvalor_avistasemipi = semipi + valor_avistasemipi
    posvalor_avistasemipiround = round(posvalor_avistasemipi, ndigits=2)
    posvalor_avistasemipiroundstr = str(posvalor_avistasemipiround)
    valor_avista = percent(posipiroundstr + "*3%")
    posvalor_avista = posipi + valor_avista
    posvalor_avistaround = round(posvalor_avista, ndigits=2)
    posvalor_avistaroundstr = str(posvalor_avistaround)
    print()
    print("Valor Unitario: R$ " + posvalor_avistasemipiroundstr + ". (Sem IPI)")
    print("Valor Unitario: R$ " + posvalor_avistaroundstr + ". (Com IPI de 3,25% incluso)")
    print()
    print("Deseja copiar o valor para colar?")
    print()
    print("1 - Sim")
    print()
    print("2 - Nao")
    print()
    while True:
        try:
            copiar = input("->")
            if copiar == "1":
                linha21 = ("Valor Unitario: R$ " + posvalor_avistasemipiroundstr + ". (Sem IPI)")
                linha22 = ("Valor Unitario: R$ " + posvalor_avistaroundstr + ". (Com IPI de 3,25% incluso)")
                clipboard.copy(linha21 + "\n" + linha22)
            if copiar == "1" or copiar == "2":
                break
            else:
                raise ValueError("Opcao invalida, tente novamente...")
        except ValueError as ve3:
            print(ve3)
    print()
    input("Pressione enter para voltar")
    exec(open("laminas/laminas_moto_ar1.py").read())
