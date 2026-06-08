"""
Projeto avaliativo P2 - Simulador de criptos ativos e carteira de investimento 
- Membros do grupo: Italo Fernandes, Gabriel Aralli, e Henry Campos
"""
#Biblioteca random para trazer aleatoriedade para o preco da cripto
import random

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cenario inicial
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
saldo_reais = float(input("Digite o valor que deseja simular: R$ ")) #Saldo em dinheiro vivo

#Dicionario que guarda o catalogo das criptos e o preco de mercado
criptos = {
    "BTC" : {"Nome": "Bitocin", "Preco": 5000.00},
    "ETH" : {"Nome": "Ethereum", "Preco": 1000.00},
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
        print("")
        print(f"{abreviacao} ({nome}): R$ {preco:.2f}")
        
def ver_carteira_de_moedas(): #Exibe patrimonio atual em reais, e valor de cripto que possui
    print(f"\nSaldo em reais: R$ {saldo_reais:.2f}")
    for abreviacao in carteira:
        qnt =  carteira[abreviacao]
        valor = qnt * criptos[abreviacao]["Preco"]
        print("")
        print(f"{abreviacao}: {qnt:.4f} unidades = R$ {valor:.2f}")
   
def comprar(abreviacao, valor_reais): #Gerencia a compra de ativos
    global saldo_reais #Permite alterar a variavel que esta fora do escopo
    if abreviacao  not in criptos: # Caso o usuario escolha uma cripto inexistente
        print("\nCripto Invalida!")
    elif valor_reais > saldo_reais: #Caso o saldo for insuficiente para a compra da cripto
        print("\nSaldo insuficiente")
    else: #Caso que realiza a compra
        preco = criptos[abreviacao]["Preco"]
        qnt = valor_reais / preco
        saldo_reais -= valor_reais
        carteira[abreviacao] += qnt
        print (f"\nCompra realizada: {qnt:.4f} {abreviacao} adicionados à carteira.")

def vender(abreviacao, qtd): #Gerencia a venda de ativos
    global saldo_reais  # Permite alterar a variável que está fora do escopo da função
    if abreviacao not in carteira: #Moeda digitada nao existe
        print("\nCripto inválida.")
    elif qtd > carteira[abreviacao]: #quantidade insuficiente para venda
        print("\nQuantidade insuficiente na carteira.")
    else: #Realiza a venda
        preco = criptos[abreviacao]["Preco"]
        total = qtd * preco             
        carteira[abreviacao] -= qtd          
        saldo_reais += total               
        print(f"\nVenda realizada: {qtd:.4f} {abreviacao} removidos da carteira de moedas.")
        
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Ciclo do mercado baseado na esolha do usuario
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print("")
print("Seja bem vindo ao simulador de cripto-ativos!")

opcao = "" #insire a variavel opcao para dar inicio ao while 

while opcao != "0":
    variar_precos() #Chama a função para variar o preço em cada ciclo do mercado
    print("\n[1]: Ver mercado.")
    print("[2]: Ver carteira de cripto-ativos.")
    print("[3]: Comprar moedas.")
    print("[4]: Vender moedas.")
    print("[0]: Sair.")
    
    opcao = input("\nEscolha uma das opções para dar sequencia: ") #Escolha a ação que deseja realizar
    
    if opcao == "1":
        ver_mercado() #Chama a função ver mercado
    elif opcao == "2":
        ver_carteira_de_moedas() #Chama a função ver carteira
    elif opcao == "3":
        ver_mercado() #Chama a função ver mercado
        abreviacao = input("\nDigite o simbolo da cripto que deseja comprar: ").upper() 
        valor_reais = float(input("Digite o valor em reais que deseja comprar: "))
        comprar(abreviacao, valor_reais) #Chama a funcao comprar com os paramentros
    elif opcao == "4":
        ver_carteira_de_moedas() #Chama a função ver carteira de criptos que o usuario tem
        abreviacao = input("\nDigite o simbolo da cripto que deseja vender: ").upper()
        qtd = float(input("Digite a quantidade de cripto que deseja vender: "))
        vender(abreviacao, qtd) #Chama a função vender com os paramentros
    else:
        print("Opção inválida. Tente novamente.")
        