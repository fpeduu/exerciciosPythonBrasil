h = float(input("Digite sua altura em metros: "))
genero = input("Você é homem ou mulher[H/M]? ")

print(f"O seu peso ideal seria {72.7 * h - 58:.2f}kg. " if genero.lower() == "h" else f"O seu peso ideal seria {62.1 * h - 44.7:.2f}kg. ")