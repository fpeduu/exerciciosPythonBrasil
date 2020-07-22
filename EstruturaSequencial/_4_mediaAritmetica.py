a, b, c, d = input("Digite as 4 notas, separadas por espaços. Ex.: 8 9 8.5 7 \n").strip().split()
a, b, c, d = float(a), float(b), float(c), float(d)
print(f"A sua média foi {(a + b + c + d)/4:.2f}. ")