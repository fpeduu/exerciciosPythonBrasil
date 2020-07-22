peso = float(input("Digite em quilos o peso da carga de peixes: "))
excesso = peso - 50
multa = excesso * 4 if excesso > 0 else 0
print(f"A carga de peixes tem {peso:.2f}kg, excedendo o máximo de 50kg em {excesso:.2f}kg. 
Isso gera uma multa de R${multa:.2f}. " if excesso > 0 else f"A carga de peixes tem {peso:.2f}, não ultrapassando o limite de 50kg. 
Tudo certo! ")