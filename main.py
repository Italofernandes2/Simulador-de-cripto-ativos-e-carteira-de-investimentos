"""
Projeto avaliativo P2 - Simulador de criptos ativos e carteira de investimento 
- Membros do grupo: Italo Fernandes, Gabriel Aralli, e Henry Campos
"""
#Biblioteca random para trazer aleatoriedade para o preco da cripto
import random

# Cenario inicial
saldo_reais = 10000.00

criptos = {
    "BTC" : {"Nome": "Bitocin", "Preco": 350000.00},
    "ETH" : {"Nome": "Ethereum", "Preco": 10000.00},
    "DOGE" : {"Nome": "Dogecoin", "Preco": 1.00},
}

carteira = {
    "BTC": 0.00,
    "ETH": 0.00,
    "DOGE": 0.00
}
"""
=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-
"""
#Funcoes do ciclo do mercado
def variar_valores():
    for abreviacao in criptos:
        variacao = random.uniform(-0.1, 0.1) #O valor vai variar de -10% a 10%
        criptos[abreviacao]["Preco"] = criptos[abreviacao]["Preco"]  * (1 + variacao) 

def ver_mercado():
    for abreviacao in criptos:
        nome = criptos[abreviacao]["Nome"]
        preco = criptos[abreviacao]["Preco"]
        print(f"{abreviacao} ({Nome}): R$ {preco}")
        
def ver_carteira_de_moedas():
    print(carteira)
   
def comprar(): 