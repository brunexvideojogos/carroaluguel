#INFORMAÇÕES PARA O CALCULO
dias_alugados = int(input("Por quantos dias o carro foi alugado?:\n"))
kms_rodados = float(input("Quantos km foram rodados?:\n").replace(",", "."))

#CALCULO DO VALOR TOTAL
preco_aluguel = dias_alugados * 60
preco_km = kms_rodados * 0.15
valor_total = preco_aluguel + preco_km

#PRINT DO RESULTADO
print("O valor total a ser pago é R$:{:.2f}".format(valor_total))
