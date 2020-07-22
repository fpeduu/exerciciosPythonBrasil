import math

largura, comprimento = input("Digite em metros a altura e o comprimento da área a ser pintada separados por espaço: ").strip().split()
largura, comprimento = float(largura), float(comprimento)

print(f"""A área a ser coberta é de {largura * comprimento}m². 
Logo, serão necessários {math.ceil(largura * comprimento/54)} latas de tinta.
Isso dá R${80 * math.ceil(largura * comprimento/54):.2f}. """)