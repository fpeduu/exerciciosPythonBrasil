valorHora = float(input("Digite o quanto você ganha por hora trabalhada em reais: "))
numHoras = int(input("Agora digite o número de horas que você trabalha por mês: "))

print(f"""+ Salário Bruto : R${valorHora * numHoras:.2f}
- IR (11%) : R${valorHora * numHoras/100 * 11:.2f}
- INSS (8%) : R${valorHora * numHoras/100 * 8:.2f}
- Sindicato (5%) : R${valorHora * numHoras/100 * 5:.2f}
= Salário Liquido : R${valorHora * numHoras - valorHora * numHoras/100 * 24:.2f}""")