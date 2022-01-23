#PROJETO SIMPLES 		
from datetime import datetime, timedelta


lista = []
texto = 'COMPRA DO MES'
nome_arquivo = f"{texto}>{datetime.now().strftime('%d-%m-%Y')}.txt"
open(nome_arquivo,'a',encoding='utf-8').write(f"         {texto}>{datetime.now().strftime('%d-%m-%Y')}\n\n\n")
while True:
	c = input('Qual produto:\n ').upper()
	
	v = float(input('Qual valor:\n '))
	q = float(input('Quantos Unidades do mesmo produto:\n '))
	t = q * round(v,2)
	lista.append(round(t,2))
	soma = sum(lista)
	print(f" {c} o valor é R$ {v} , voce comprou {q} unidade, {q} * {v} = total é R$ {round(t,2)}")
	for i in range(int(q)):
		print(f'Produto {i +1} : {c} | Valor : {v} ')
		open(nome_arquivo,'a',encoding='utf-8').write(f" >> Produto : {c} | Valor : R$ {v}\n")
	open(nome_arquivo,'a',encoding='utf-8').write(f'*** {c} o Total fica em R$ {round(t,2)}\n{"<=>"*25}\n')
	print(f'>>{c} o Total fica em R$  {round(t,2)}')
	soma = sum(lista)
	print(f'** Sua Compra até o momento está em R$ {round(soma,2)}')
	resp = ' '
	while resp not in 'SN':
	    resp = str(input('>>Quer Continuar:[S/N] ')).strip().upper()[0]
	if resp == 'N':
	    break
print('***Obrigado por usar nossos serviços...***')
open(nome_arquivo,'a',encoding='utf-8').write(f"{'='*40}\n***  Total da compra R$ {round(soma,2)}\n")
soma = sum(lista)
print(soma)
