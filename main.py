"""
Projeto avaliativo P2 - Simulador de criptos ativos e carteira de investimento 
- Membros do grupo: Italo Fernandes, Gabriel Aralli, e Henry Campos
"""
#Biblioteca random para trazer aleatoriedade para o preco da cripto
import random

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cenario inicial
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
saldo_reais = 10000.00 #Saldo em dinheiro vivo

#Dicionario que guarda o catalogo das criptos e o preco de mercado
criptos = {
    "BTC" : {"Nome": "Bitocin", "Preco": 350000.00},
    "ETH" : {"Nome": "Ethereum", "Preco": 10000.00},
    "DOGE" : {"Nome": "Dogecoin", "Preco": 1.00},
}
#Carteira do usuario que armazena a qntd. de cada moeda
carteira = {
    "BTC": 0.00,
    "ETH": 0.00,
    "DOGE": 0.00
}

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Funcoes do ciclo do mercado
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def variar_precos(): #Essa funcao vai simular a volatividade do mercado
    for abreviacao in criptos:
        variacao = random.uniform(-0.1, 0.1) #O valor vai variar de -10% a 10%
        criptos[abreviacao]["Preco"] = criptos[abreviacao]["Preco"]  * (1 + variacao) 

def ver_mercado(): #Exibe o nome e o preco atual da cripto
    for abreviacao in criptos:
        nome = criptos[abreviacao]["Nome"]
        preco = criptos[abreviacao]["Preco"]
        print(f"{abreviacao} ({nome}): R$ {preco:.2f}")
        
def ver_carteira_de_moedas(): #Exibe patrimonio atual em reais, e valor de cripto que possui
    print(f"Saldo em reais: R$ {saldo_reais:.2f}")
    for abreviacao in carteira:
        qnt =  carteira[abreviacao]
        valor = qnt * criptos[abreviacao]["Preco"]
        print(f"{abreviacao}: {qnt:.2f} unidades = R$ {valor:.2f}")
   
def comprar(abreviacao, valor_reais): #Gerencia a compra de ativos
    global saldo_reais #Permite alterar a variavel que esta fora do escopo
    if abreviacao  not in criptos: # Caso o usuario escolha uma cripto inexistente
        print("Cripto Invalida!")
    elif valor_reais > saldo_reais: #Caso o saldo for insuficiente para a compra da cripto
        print("Saldo insuficiente")
    else: #Caso que realiza a compra
        preco = criptos[abreviacao]["Preco"]
        qnt = valor_reais / preco
        saldo_reais -= valor_reais
        carteira[abreviacao] += qnt
        print (f" Comprado {qnt:.2f} {abreviacao} por R$ {valor_reais:.2f}")

def vender(abreviacao, qtd): #Gerencia a venda de ativos
    global saldo_reais  # Permite alterar a variável que está fora do escopo da função
    if abreviacao not in carteira: #Moeda digitada nao existe
        print("Cripto inválida.")
    elif qtd > carteira[abreviacao]: #quantidade insuficiente para venda
        print("Quantidade insuficiente na carteira.")
    else: #Realiza a venda
        preco = criptos[abreviacao]["Preco"]
        total = qtd * preco             
        carteira[abreviacao] -= qtd          
        saldo_reais += total               
        print(f"Vendido {qtd:.4f} {abreviacao} por R$ {total:.2f}")