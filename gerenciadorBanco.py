class GerenteBanco():
    
    def __init__(self, saldo):
        self.saldo = saldo
    
    def fazerDeposito(self, valor):
        self.saldo += valor
        print(f"{valor} adicionado a conta")
        
    def fazerSaque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"{valor} removido da conta") 
        else:
            print(f"Saldo insuficiente (faltam {valor - self.saldo}R$)")
            
            
            
            