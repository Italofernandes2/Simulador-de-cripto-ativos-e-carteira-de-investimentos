"""
Projeto avaliativo P2 - Simulador de criptos ativos e carteira de investimento 
- Membros do grupo: Italo Fernandes, Gabriel Aralli, e Henry
"""
#Biblioteca random para trazer aleatoriedade para o preco da cripto
import random

# Cenario inicial
saldo_reais = 10000.00
criptos = {
    "BTC" : {"Nome": "Bitocin", "Preco": 300000.00},
    "ETH" : {"Nome": "Ethereum", "Preco": 15000.00},
    "DOGE" : {"Nome": "Dogecoin", "Preco": 1.20},
}
carteira = {
    "BTC": 0.00,
    "ETH": 0.00,
    "DOGE": 0.00
}