import math

largura, comprimento = input("Digite em metros a altura e o comprimento da área a ser pintada separados por espaço: ").strip().split()
largura, comprimento = float(largura), float(comprimento)

precoLataGalao = 80 * (math.ceil(largura * comprimento/108 - largura * comprimento % 108/108)) + 25 * math.ceil(largura * comprimento % 108/21.6)
precoLataGalaoAcrescimo = precoLataGalao + precoLataGalao/10

print(f"""A área a ser coberta é de {largura * comprimento}m². 
Logo, serão necessários {math.ceil(largura * comprimento/108)} latas de tinta, que equivalem a R${80 * math.ceil(largura * comprimento/108):.2f};
ou {math.ceil(largura * comprimento/21.6)} galões de tinta, que equivalem a R${25 * math.ceil(largura * comprimento/21.6):.2f};
ou {math.ceil((largura * comprimento/108) - largura * comprimento % 108/108)} latas de tinta e {math.ceil(largura * comprimento % 108/21.6)} galões de tinta,
que equivalem, com um acréscimo de 10% de folga, a R${precoLataGalaoAcrescimo:.2f}. """)