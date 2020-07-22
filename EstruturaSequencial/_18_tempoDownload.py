tamanho = float(input("Digite em Mb o tamanho do arquivo a ser baixado: "))
velocidade = float(input("Digite em Mbps a velocidade da internet que será utilizada: "))

print(f"O arquivo será baixaado em, aproximadamente, {tamanho/velocidade/60:.1f}min. ")