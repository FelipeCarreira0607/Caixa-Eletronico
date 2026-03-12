from gerenciadorBanco import *
import tkinter as tk
from sqlite3 import *

#Configuraçao da janela
janela = tk.Tk()
janela.geometry("600x400")

janela.mainloop()


# logica dos processos
usuario = GerenteBanco(1000.0)
    
while True:
    print("-"*10)
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Sair")
    print("-"*10)
    operacao = int(input(""))

    match operacao:
        case 1:
            valor = float(input("Insira o valor do deposito: "))
            usuario.fazerDeposito(valor)
            print(f"Saldo atua: {usuario.saldo}")
        case 2:
            valor = float(input("Insira o valor do saque: "))
            usuario.fazerSaque(valor)
            print(f"Saldo atua: {usuario.saldo}")
        case 3:
            print("Encerrado...")
            break
        
        
        
