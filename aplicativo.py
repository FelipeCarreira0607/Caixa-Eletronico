import tkinter as tk

# # class TelaLogin:
#     def __init__(self, cpf_conta, senha, master=None):

#         self.pag = master
#         self.cpf_conta = cpf_conta
#         self.senha = senha

#         #Parte do app
#         self.container1 = tk.Frame(self.pag)
#         self.container1.pack()

#         self.container2 = tk.Frame(self.pag)
#         self.container2.pack()

#         self.container3 = tk.Frame(self.pag)
#         self.container3.pack()

#         self.container4 = tk.Frame(self.pag)
#         self.container4.pack()

#         self.container5 = tk.Frame(self.pag)
#         self.container5.pack()

#         self.txt_login = tk.Label(self.container1)
#         self.txt_login["text"] = "Informe suas credenciais: "
#         self.txt_login.pack()

#         self.txt_cpf = tk.Label(self.container2)
#         self.txt_cpf["text"] = "CPF: "
#         self.txt_cpf.pack()
#         self.entry_cpf = tk.Entry(self.container2)
#         self.entry_cpf.pack()

#         self.txt_senha = tk.Label(self.container3)
#         self.txt_senha["text"] = "Senha: "
#         self.txt_senha.pack()
#         self.entry_senha = tk.Entry(self.container3)
#         self.entry_senha.pack()

#         self.botao_entrar = tk.Button(self.container4)
#         self.botao_entrar["text"] = "Entrar"
#         self.botao_entrar["command"] = self.verifCredencial
#         self.botao_entrar.pack()

#         self.txt_login = tk.Label(self.container5)
#         self.txt_login.pack()

#     def verifCredencial(self):
#         if self.cpf_conta == self.entry_cpf.get() and self.senha == self.entry_senha.get():
#             self.txt_login["text"] = "Login realizado com sucesso! "

#         else:
#             self.txt_login["text"] = "Credenciais invalidas! "

class TelaOperacoes:
    def __init__(self, master=None):

        self.container1 = tk.Frame(master)
        self.container1.pack()

        self.container2 = tk.Frame(master)
        self.container2.pack()

        self.container3 = tk.Frame(master)
        self.container3.pack()

        self.container4 = tk.Frame(master)
        self.container4.pack()

        self.txt_pedido = tk.Label(self.container1)
        self.txt_pedido["text"] = "Selecione a operação: "
        self.txt_pedido.pack()

        self.txt_deposito = tk.Label(self.container2)
        self.txt_deposito["text"] = "Deposito"
        self.txt_deposito.pack(side="left")
        self.btn_deposito = tk.Button(self.container3)
        self.btn_deposito.pack(side="left")

        self.txt_saque = tk.Label(self.container2)
        self.txt_saque["text"] = "Saque"
        self.txt_saque.pack(side="right")
        self.btn_saque = tk.Button(self.container3)
        self.btn_saque.pack(side="right")





class Aplicativo:
    def __init__(self):
        pass


janela = tk.Tk()


# TelaLogin("13013342269", "123", janela)
TelaOperacoes(janela)


janela.mainloop() 