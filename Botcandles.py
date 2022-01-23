from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime
from dateutil import tz
import getpass
from colorama import init, Fore, Back, Style


init(convert=True)

print(Style.BRIGHT + Fore.RED +'''	
                                ██████   ██████  ████████     ██  ██████                                   
                                ██   ██ ██    ██    ██        ██ ██    ██                                  
                                ██████  ██    ██    ██        ██ ██    ██                                  
                                ██   ██ ██    ██    ██        ██ ██ ▄▄ ██                                  
                                ██████   ██████     ██        ██  ██████                                   
                                                                     ▀▀                                    
                                                                                                           
    ██████  ██████   ██████  ██████   █████  ██████  ██ ██      ██ ██████   █████  ██████  ███████ ███████ 
    ██   ██ ██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██ ██      ██ ██   ██ ██   ██ ██   ██ ██      ██      
    ██████  ██████  ██    ██ ██████  ███████ ██████  ██ ██      ██ ██   ██ ███████ ██   ██ █████   ███████ 
    ██      ██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██ ██      ██ ██   ██ ██   ██ ██   ██ ██           ██ 
    ██      ██   ██  ██████  ██████  ██   ██ ██████  ██ ███████ ██ ██████  ██   ██ ██████  ███████ ███████ 
                                                                                                           
	
    produzido por @denissousapereira & @poolals
	Os Timeframe(MINUTOS dos CANDLES(Velas)) são:
	1 Minuto > Irá Digita == 1
	2 Minuto > Irá Digita == 2
	5 Minuto > Irá Digita == 5
	15 Minuto > Irá Digita == 15
	1 HORA > Irá Digita == 60
	2 HORA > Irá Digita == 120
	4 HORA > Irá Digita == 240
	12 HORA > Irá Digita == 720
	1 DIA > Irá Digita == 1440
    ''' +Style.RESET_ALL  )                                                                                         
print(Style.BRIGHT + Fore.YELLOW + '|---------------------------------------Bem vindo--------------------------------------------|'+ Style.RESET_ALL)
print(Style.BRIGHT + Fore.YELLOW + '|                                                                                            |'+ Style.RESET_ALL)		
print(Style.BRIGHT + Fore.YELLOW + '|Esse bot foi feito pra te auxiliar a buscar aonde teve mais toques nas taxas.               |'+ Style.RESET_ALL)
print(Style.BRIGHT + Fore.YELLOW + '|Sempre Use as Taxas para te auxiliar nas entradas,use sempre confluencias com Indicadores.  |'+ Style.RESET_ALL)
print(Style.BRIGHT + Fore.RED + '|_____________________Venda PROIBIDA_________________________________________________________|'+ Style.RESET_ALL)	

print(Style.BRIGHT + Fore.YELLOW + '''CONECTAR-SE A CORRETORA:
'''+ Style.RESET_ALL)

print(Style.BRIGHT + Fore.YELLOW +'=-='*40 + Style.RESET_ALL)
while True:

	#email = str(input('***DIGITE SEU EMAIL: '))
	#print(Style.BRIGHT + Fore.BLUE + '***DIGITE SEU EMAIL: ' + Fore.RESET)
	#email = str(input('  '))
	#print(Style.BRIGHT + Fore.BLUE + '***DIGITE SUA SENHA DA IQ: ' + Fore.RESET)
	#senha = str(input('   '))
	#senha = str(input('***DIGITE SUA SENHA DA IQ:'))
	print('=-='*40)
	print('=-='*40)
	API = IQ_Option('email', 'senha')
	API.connect()
	print('=-='*40)
	print('=-='*40)
	if API.check_connect():
		print(Style.BRIGHT + Fore.GREEN + '\n***Conectado com sucesso!***'+ Style.RESET_ALL)
		API.change_balance('PRACTICE') # PRACTICE / REAL 
		break


	else:
		print(Style.BRIGHT + Fore.RED +'\n***Dados incorretos, tente novamente!!!!!'+ Style.RESET_ALL)
		input('\n***Aperte enter para tentar novamente. \n')
print('=-='*40)        
time.sleep(1)




def perfil(): # Função para capturar informações do perfil
	perfil = json.loads(json.dumps(API.get_profile_ansyc()))
	
def timestamp_converter(x): # Função para converter timestamp
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))
	
	return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-3]
	
def banca():
	return API.get_balance()

#retorna pra catalogar
print(Fore.YELLOW +'______________________________________________________________________________________________'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|           *********Seja bem vindo bora puxa os dados dessa IQ_Option**************         |'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|                                                                                            |'+ Fore.RESET)
print(Fore.YELLOW +'|____________________________________________________________________________________________|'+ Fore.RESET)

while True:

	print(Style.BRIGHT + Fore.BLUE + '>>Indique a Paridade: ' + Fore.RESET)
	par = input('   ').strip().upper()
	print(Style.BRIGHT + Fore.BLUE + '>>Indique o Timeframe: ' + Fore.RESET)
	timeframe = int(input('   '))
	print(Style.BRIGHT + Fore.BLUE + '>>Indique Quantas Velas: ' + Fore.RESET)
	candles = int(input('   '))
	print(Style.BRIGHT + Fore.BLUE + '>>Indique Quantos Toques: ' + Fore.RESET)
	toque = int(input('   '))
	print('=-='*40)
	#vela atual
	velas_atual = API.get_candles(par, timeframe * 60, 4, time.time())
	
	preco_atual = velas_atual[3]['close']
	preco_compra = float(preco_atual  * 0.003 / 100 ) 
	preco_venda = float(preco_atual * 0.003 / 100 ) 
	preco_put = round(( preco_compra + preco_atual),6)
	preco_call = round((preco_venda - preco_atual),6)* -1
	

		
	print(f'PREÇO ATUAL: {preco_atual}')
	print(f'Taxas acima {preco_put} melhor para PUT(VENDA)')
	print(f'Taxas abaixo {preco_call} melhor para CALL(COMPRA)')
	print('=-='*40)
	lista4 = []
	x = []

	vela = API.get_candles(par, timeframe * 60 , (int(candles)), time.time())

	for velas in vela:
		# aqui faz adciona a lista que esta vazia

		lista4.append(velas['min' and 'max' and 'open' and 'close'])
	

		if lista4.count(velas['min' and 'max' and 'open' and 'close']) >= toque :
			lista = []
			lista.append(str(lista4))
			print(Style.BRIGHT + Fore.GREEN + '|***TOQUE:',lista4.count(velas['min' and 'max' and 'open' and 'close']),'  | TAXA =>',str(velas['min' and 'max' and 'open' and 'close']),'|','Par:',par,'|Timeframe:',timeframe,',Qnt Velas:',candles,'============|'+ Fore.RESET)
			#print('|                                                                                          |')
			print(Fore.RED  +'|==============|=================|============================================================|'+ Fore.RESET)
			
			print('Maiores Toques:',str(velas['max' and 'min' and 'open' and 'close']))
			
	print(f'PREÇO ATUAL: {preco_atual}')
	print(f'Taxas acima {preco_put} melhor para PUT(VENDA)')
	print(f'Taxas abaixo {preco_call} melhor para CALL(COMPRA)')
	print('=-='*40)
			

	resp = ' '
	while resp not in 'SN':
	    resp = str(input('>>Quer Continuar:[S/N] ')).strip().upper()[0]
	if resp == 'N':
	    break
print('***Obrigado por usar nossos serviços...***')			
