a, b = input("Digite dois números inteiros* separados por espaço: ").strip().split()
a, b = int(a), int(b)
c = float(input("Digite um número real*: "))

print(f"O produto do dobro de {a} com metade de {b} é igual a {2 * a * (b/2)}. ")
print(f"A soma do triplo de {a} com {c} é igual a {3 * a + c:.1f}. ")
print(f"{c} elevado ao cubo é igual a {c**3:.2f}")